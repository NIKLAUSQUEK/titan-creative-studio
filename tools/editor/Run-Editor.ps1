<#
.SYNOPSIS
  TITAN auto-editor on your PC: raw footage -> strategist brief -> edit recipe -> cheap draft -> chat revisions -> 1080p finals.
  Runs locally with your Claude Code login (claude -p). No API keys, no API credits.

.DESCRIPTION
  First run installs ffmpeg + Python (winget), then faster-whisper, PyTorch (CPU, or CUDA if you have an NVIDIA GPU) and open_clip
  into %LOCALAPPDATA%\TitanEditor\venv. Every step is resumable; re-running skips finished work.
    ingest   : word timestamps, fillers, silences, scene cuts, best takes, hook shortlist, contact sheets (local, free)
    brief    : strategist edit brief: goal, audience, platform, 5 ranked hooks, beats, CTA, compliance (one claude -p call)
    broll    : local CLIP index of your footage folders (incl. G:\My Drive\...); Claude only picks among the top 3 per beat
    assemble : edit.v1.json from brief + preset + brand guide
    draft    : lowest-quality render of every aspect, then QC (contact sheets + checks)

.EXAMPLE
  .\Run-Editor.ps1 -Organize "G:\My Drive\Photos","D:\Phone backup"
  (AI-organise a whole photo/video library, locally and free: categories, people, events, best picks, sensitive flags.
   Opens REVIEW.html. Originals are never moved. Add -Llm claude-cli to also name each event from one contact sheet.)
  .\Run-Editor.ps1 -NameFace 1,klaus            (name a face cluster from people_sheet.jpg; consent "yes" for you)
  .\Run-Editor.ps1 -OrganizedTo "D:\Organised"   (copy/hardlink best picks into Category\Event folders)

.EXAMPLE
  .\Run-Editor.ps1 -SelfTest
  (synthetic end-to-end test; proves the install works)

.EXAMPLE
  .\Run-Editor.ps1 -BrollRoots "G:\My Drive\clinic_broll","D:\Footage\B-roll" -Steps broll-index
  (index B-roll once; later runs only add new files)

.EXAMPLE
  .\Run-Editor.ps1 -Project back-pain-myth -Footage "D:\Shoots\2026-10-24" -Brand physio-spot -Goal expert -Platform tiktok -Ask "myth-bust for men 30-45"

.EXAMPLE
  .\Run-Editor.ps1 -Project back-pain-myth -Revise "cut first 2 s, punchier captions"
  .\Run-Editor.ps1 -Project back-pain-myth -Chat            (type notes, get a new draft each time)
  .\Run-Editor.ps1 -Project back-pain-myth -Approve -Final  (1080p finals of every aspect + QC + handoff for /publish)
#>
[CmdletBinding()]
param(
  [string] $Project = "",
  [string[]] $Footage = @(),
  [string] $Brand = "",
  [string] $Goal = "",                       # wise | expert | trust | sell | founder | entertain
  [string] $Platform = "",                   # tiktok | reels | shorts | youtube | linkedin | feed
  [string] $Preset = "",                     # see: .\Run-Editor.ps1 -Presets
  [string] $Ask = "",                        # what you want, in plain words
  [string] $Aspects = "",                    # e.g. "9:16,1:1,16:9" (default: brief's platform + extras)
  [string] $Music = "",                      # path to a licensed/original track
  [string] $MusicLicence = "",               # original | licensed:<source> | in-app
  [string[]] $BrollRoots = @(),
  [string] $IndexDir = (Join-Path $env:LOCALAPPDATA "TitanEditor"),
  [string] $CreatorBrainWork = (Join-Path $env:LOCALAPPDATA "CreatorBrain"),
  [string[]] $Steps = @("ingest", "brief", "broll", "assemble", "draft"),
  [string] $Revise = "",
  [switch] $Chat,
  [switch] $Approve,
  [switch] $Final,
  [switch] $SelfTest,
  [switch] $Presets,
  [ValidateSet("auto", "tiny", "base", "small", "medium", "large-v3")] [string] $WhisperModel = "auto",
  [ValidateSet("claude-cli", "none")] [string] $Llm = "claude-cli",
  [string] $ClaudeModel = "",                # sonnet (cheaper) | opus; empty = your Claude Code default
  [string[]] $Organize = @(),                # folders of photos/videos to AI-organise
  [string[]] $NameFace = @(),                # e.g. -NameFace 1,klaus
  [string] $OrganizedTo = "",                # build an organised copy/hardlink tree here
  [switch] $SkipInstall
)
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$py = Join-Path $here "editor.py"
$work = Join-Path $env:LOCALAPPDATA "TitanEditor"
New-Item -ItemType Directory -Force -Path $work | Out-Null
Start-Transcript -Path (Join-Path $work ("run-" + (Get-Date -Format "yyyyMMdd-HHmmss") + ".log")) | Out-Null
function Have($cmd) { [bool](Get-Command $cmd -ErrorAction SilentlyContinue) }
function Refresh-Path { $env:Path = [Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [Environment]::GetEnvironmentVariable("Path", "User") }

try {
  # ---------- one-time setup (same pattern as tools/creator-brain) ----------
  if (-not $SkipInstall) {
    if (-not (Have "ffmpeg")) { Write-Host "Installing ffmpeg (winget)..." -ForegroundColor Cyan; winget install --id Gyan.FFmpeg -e --accept-source-agreements --accept-package-agreements | Out-Host; Refresh-Path }
    if (-not (Have "python") -and -not (Have "py")) { Write-Host "Installing Python 3.12 (winget)..." -ForegroundColor Cyan; winget install --id Python.Python.3.12 -e --accept-source-agreements --accept-package-agreements | Out-Host; Refresh-Path }
  }
  if (-not (Have "ffmpeg")) { throw "ffmpeg not found. winget install Gyan.FFmpeg, reopen PowerShell, run again." }
  $venv = Join-Path $work "venv"
  $vpy = Join-Path $venv "Scripts\python.exe"
  if (-not (Test-Path $vpy)) {
    Write-Host "Creating Python environment in $venv ..." -ForegroundColor Cyan
    if (Have "py") { py -3 -m venv $venv } else { python -m venv $venv }
  }
  $stamp = Join-Path $work "deps.ok"
  if (-not $SkipInstall -and -not (Test-Path $stamp)) {
    & $vpy -m pip install --quiet --upgrade pip
    & $vpy -m pip install --quiet faster-whisper pillow numpy "opencv-python-headless<5" rembg   # opencv YuNet/SFace = face grouping in organize
    # torch + torchvision from the same index first, so open_clip doesn't pull a mismatched torchvision
    $idx = if (Have "nvidia-smi") { "https://download.pytorch.org/whl/cu124" } else { "https://download.pytorch.org/whl/cpu" }
    Write-Host "Installing PyTorch ($idx) + open_clip (one-time, ~1-3 GB)..." -ForegroundColor Cyan
    & $vpy -m pip install --quiet torch torchvision --index-url $idx
    & $vpy -m pip install --quiet open_clip_torch
    if ($LASTEXITCODE -eq 0) { Set-Content $stamp (Get-Date) }
  }
  if ($Llm -eq "claude-cli" -and -not (Have "claude")) {
    throw "Claude Code CLI not found. Install Node.js LTS, then: npm install -g @anthropic-ai/claude-code ; run 'claude' once to sign in. (Or use -Llm none for local-only heuristics.)"
  }
  $env:PYTHONUTF8 = "1"
  $base = @($py)
  if ($Project) { $base += @("--project", $Project) }
  $llmArgs = @("--llm", $Llm); if ($ClaudeModel) { $llmArgs += @("--claude-model", $ClaudeModel) }
  function Ed([string[]] $a) { & $vpy @($base + $a); if ($LASTEXITCODE) { throw "editor step failed: $($a -join ' ') (log in $work)" } }

  if ($SelfTest) { & $vpy $py selftest --whisper-model tiny; exit $LASTEXITCODE }
  if ($Presets) { Ed @("preset", "list"); return }
  if ($Organize.Count -gt 0) {
    $orgLlm = if ($PSBoundParameters.ContainsKey("Llm")) { $Llm } else { "none" }   # local-only unless you ask for event names
    Ed (@("organize", "run") + $Organize + @("--index-dir", $IndexDir, "--llm", $orgLlm))
    Ed @("organize", "export-library", "--person", "klaus", "--index-dir", $IndexDir)
    Start-Process (Join-Path $IndexDir "organize\REVIEW.html"); Start-Process (Join-Path $IndexDir "organize\people_sheet.jpg"); return
  }
  if ($NameFace.Count -ge 2) {
    Ed @("organize", "name", $NameFace[0], $NameFace[1], "--index-dir", $IndexDir); Ed @("organize", "report", "--index-dir", $IndexDir)
    Ed @("organize", "export-library", "--person", $NameFace[1].ToLower(), "--index-dir", $IndexDir); return
  }
  if ($OrganizedTo) { Ed @("organize", "apply", "--to", $OrganizedTo, "--index-dir", $IndexDir); Start-Process $OrganizedTo; return }
  & $vpy @($base + @("check"))

  if ($BrollRoots.Count -gt 0) {
    $a = @("broll-index") + $BrollRoots + @("--index-dir", $IndexDir)
    if (Test-Path $CreatorBrainWork) { $a += @("--creator-brain-work", $CreatorBrainWork) }
    Ed $a
    if ($Steps.Count -eq 1 -and $Steps[0] -eq "broll-index") { return }
  }
  if ($Revise) { Ed (@("revise", $Revise) + $llmArgs); Ed @("render"); Ed @("qc"); return }
  if ($Chat) { & $vpy @($base + @("chat") + $llmArgs); return }
  if ($Approve) { Ed @("approve") }
  if ($Final) {
    Ed @("render", "--final"); Ed @("qc", "--final"); Ed @("handoff")
    Write-Host "`nFinals ready. Next in Claude Code: /publish" -ForegroundColor Green; return
  }
  if ($Approve) { return }
  if (-not $Project) { throw "Pass -Project <name> (a folder under projects\)." }

  $wm = @("--whisper-model", $WhisperModel)
  if ($Steps -contains "ingest") {
    if ($Footage.Count -eq 0) { Write-Host "No -Footage given: reusing what was ingested before." -ForegroundColor DarkGray }
    else { Ed (@("ingest") + $Footage + $wm) }
  }
  if ($Steps -contains "brief") {
    $a = @("brief") + $llmArgs
    foreach ($kv in @(@("--brand", $Brand), @("--goal", $Goal), @("--platform", $Platform), @("--preset", $Preset), @("--ask", $Ask))) { if ($kv[1]) { $a += $kv } }
    Ed $a
  }
  if ($Steps -contains "broll") { Ed (@("broll-match", "--index-dir", $IndexDir) + $llmArgs) }
  if ($Steps -contains "assemble") {
    $a = @("assemble")
    foreach ($kv in @(@("--preset", $Preset), @("--aspects", $Aspects), @("--music", $Music), @("--music-licence", $MusicLicence))) { if ($kv[1]) { $a += $kv } }
    Ed $a
  }
  if ($Steps -contains "draft") { Ed @("render"); Ed (@("qc") + $llmArgs) }
  $p = Join-Path (Split-Path (Split-Path $here)) "projects\$Project\autoedit"
  Write-Host "`nDraft ready. Brief: $p\EDIT_BRIEF.md  Renders: $p\renders  QC: $p\qc" -ForegroundColor Green
  Write-Host "Revise: .\Run-Editor.ps1 -Project $Project -Revise `"cut first 2 s, punchier captions`"   or  -Chat" -ForegroundColor DarkGray
}
finally { Stop-Transcript | Out-Null }
