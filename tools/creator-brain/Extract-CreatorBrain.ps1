<#
.SYNOPSIS
  Turns Klaus's video/photo folders into a readable Obsidian "Creator Brain".

.DESCRIPTION
  1. extract : finds every video/audio/photo under -Source, reads its metadata (date, device, GPS),
               makes a 3x3 contact sheet of frames, and transcribes speech locally with faster-whisper.
  2. sense   : Claude reads each transcript + contact sheet and returns structured notes
               (summary, era, people, themes, emotions, verbatim quotes, story seeds, hooks,
               values/beliefs, wisdom notes, content ideas, techniques to borrow from reference creators).
  3. vault   : writes an Obsidian vault: one note per media item + Home, Eras, Themes, People,
               Quotes, Hooks, Story Seeds, Values, Wisdom Notes, Content Ideas.
  Every step is resumable. Re-run any time; only new files are processed.

.EXAMPLE
  .\Extract-CreatorBrain.ps1 -Source "D:\Creator Brain","G:\My Drive\mens_health_social" -Limit 5
  (test on 5 files first, then run again without -Limit)

.EXAMPLE
  .\Extract-CreatorBrain.ps1 -Source "D:\Creator Brain" -Steps vault
#>
[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)] [string[]] $Source,
  [string] $Vault = (Join-Path $HOME "Documents\Obsidian\Klaus Brain"),
  [string] $Work = (Join-Path $env:LOCALAPPDATA "CreatorBrain"),
  [ValidateSet("auto", "tiny", "base", "small", "medium", "large-v3")] [string] $WhisperModel = "auto",
  [string] $Language = "",                       # "" = auto-detect per file; "en" forces English
  [ValidateSet("claude-cli", "api")] [string] $Llm = "claude-cli",
  [string] $ClaudeModel = "",                    # e.g. "sonnet" or "opus"; empty = your Claude Code default
  [string[]] $Steps = @("extract", "sense", "vault"),
  [int] $Limit = 0,
  [ValidateSet("life", "course")] [string] $Mode = "life",   # course = lessons -> frameworks, templates, action items
  [switch] $SkipInstall
)
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$py = Join-Path $here "creator_brain.py"
New-Item -ItemType Directory -Force -Path $Work, $Vault | Out-Null
$logFile = Join-Path $Work ("run-" + (Get-Date -Format "yyyyMMdd-HHmmss") + ".log")
Start-Transcript -Path $logFile | Out-Null

function Have($cmd) { [bool](Get-Command $cmd -ErrorAction SilentlyContinue) }
function Refresh-Path { $env:Path = [Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [Environment]::GetEnvironmentVariable("Path", "User") }

try {
  foreach ($s in $Source) { if (-not (Test-Path -LiteralPath $s)) { throw "Source not found: $s" } }

  # Unzip any .zip files found in the sources (once) into the work folder and add them as sources
  $unz = Join-Path $Work "unzipped"
  $extra = @()
  foreach ($s in $Source) {
    $zips = if ((Get-Item -LiteralPath $s).PSIsContainer) { Get-ChildItem -LiteralPath $s -Recurse -Filter *.zip -File } else { Get-Item -LiteralPath $s | Where-Object Extension -eq ".zip" }
    foreach ($z in $zips) {
      $dest = Join-Path $unz $z.BaseName
      if (-not (Test-Path $dest)) {
        Write-Host "Unzipping $($z.Name) ..." -ForegroundColor Cyan
        Expand-Archive -LiteralPath $z.FullName -DestinationPath $dest -Force
      }
      $extra += $dest
    }
  }
  $Source = @($Source | Where-Object { -not ((Test-Path -LiteralPath $_ -PathType Leaf) -and $_ -like "*.zip") }) + $extra

  # ---------- one-time setup ----------
  if (-not $SkipInstall) {
    if (-not (Have "ffmpeg")) {
      Write-Host "Installing ffmpeg (winget)..." -ForegroundColor Cyan
      winget install --id Gyan.FFmpeg -e --accept-source-agreements --accept-package-agreements | Out-Host
      Refresh-Path
    }
    if (-not (Have "python") -and -not (Have "py")) {
      Write-Host "Installing Python 3.12 (winget)..." -ForegroundColor Cyan
      winget install --id Python.Python.3.12 -e --accept-source-agreements --accept-package-agreements | Out-Host
      Refresh-Path
    }
  }
  if (-not (Have "ffmpeg")) { throw "ffmpeg not found. Install it (winget install Gyan.FFmpeg), reopen PowerShell, run again." }

  $venv = Join-Path $Work "venv"
  $vpy = Join-Path $venv "Scripts\python.exe"
  if (-not (Test-Path $vpy)) {
    Write-Host "Creating Python environment in $venv ..." -ForegroundColor Cyan
    if (Have "py") { py -3 -m venv $venv } else { python -m venv $venv }
  }
  if (-not $SkipInstall) {
    & $vpy -m pip install --quiet --upgrade pip
    & $vpy -m pip install --quiet faster-whisper pillow pillow-heif numpy
  }

  if ($WhisperModel -eq "auto") {
    $WhisperModel = if (Have "nvidia-smi") { "large-v3" } else { "small" }
    Write-Host "Whisper model: $WhisperModel (use -WhisperModel medium for better Singlish/Chinese on a fast PC)" -ForegroundColor DarkGray
  }

  if ($Steps -contains "sense") {
    if ($Llm -eq "claude-cli" -and -not (Have "claude")) {
      throw "Claude Code CLI not found. Install Node.js, then: npm install -g @anthropic-ai/claude-code ; run 'claude' once to sign in. Or use -Llm api with `$env:ANTHROPIC_API_KEY set."
    }
    if ($Llm -eq "api" -and -not $env:ANTHROPIC_API_KEY) { throw "Set `$env:ANTHROPIC_API_KEY first (never paste it into files)." }
  }

  # ---------- run ----------
  $env:PYTHONUTF8 = "1"
  if ($Steps -contains "extract") {
    $a = @($py, "extract", "--work", $Work, "--model", $WhisperModel, "--src") + $Source
    if ($Language) { $a += @("--language", $Language) }
    if ($Limit) { $a += @("--limit", $Limit) }
    & $vpy @a
    if ($LASTEXITCODE) { throw "extract failed (see $logFile)" }
  }
  if ($Steps -contains "sense") {
    $a = @($py, "sense", "--work", $Work, "--llm", $Llm, "--mode", $Mode)
    if ($ClaudeModel) { $a += @("--model", $ClaudeModel) }
    if ($Limit) { $a += @("--limit", $Limit) }
    & $vpy @a
    if ($LASTEXITCODE) { throw "sense failed (see $logFile)" }
  }
  if ($Steps -contains "vault") {
    $folder = if ($Mode -eq "course") { "Course Brain" } else { "Creator Brain" }
    & $vpy $py vault --work $Work --vault $Vault --mode $Mode --folder $folder
    if ($LASTEXITCODE) { throw "vault failed (see $logFile)" }
    Write-Host "`nDone. In Obsidian: Open folder as vault -> $Vault -> '$folder/00 Home'" -ForegroundColor Green
  }
}
finally {
  Stop-Transcript | Out-Null
}
