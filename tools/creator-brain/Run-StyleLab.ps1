<#
.SYNOPSIS
  Builds the creator Style DNA library on your PC for free: no vidIQ credits.
  It downloads each creator's top videos (yt-dlp), measures cuts and pacing (ffmpeg), transcribes them
  (faster-whisper), has Claude break each one down, and synthesises one StyleCard per creator.

.EXAMPLE
  .\Run-StyleLab.ps1 -Batch 4 -Per 3 -Browser chrome
  (creators from Supabase batch 4, 3 videos each, using your Chrome login so YouTube/IG/TikTok don't block you)

.EXAMPLE
  .\Run-StyleLab.ps1 -Creators .\my-creators.json -Steps fetch,analyse,cards,push
#>
[CmdletBinding()]
param(
  [string] $Creators = "",                 # JSON list; empty = pull from Supabase (needs env vars) into Work\creators.json
  [int] $Batch = 0,                        # Supabase batch to pull (0 = all)
  [int] $Per = 3,                          # videos per creator
  [string] $Browser = "chrome",            # cookies source for YouTube/IG/TikTok: chrome | edge | firefox | "" (none)
  [string] $Work = (Join-Path $env:LOCALAPPDATA "CreatorBrain\stylelab"),
  [string] $WhisperModel = "small",
  [string] $ClaudeModel = "",
  [string[]] $Steps = @("fetch", "analyse", "cards", "push"),
  [switch] $DeleteVideos,                  # delete each video after analysis (saves disk)
  [switch] $SkipInstall
)
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$py = Join-Path $here "style_lab.py"
$venv = Join-Path $env:LOCALAPPDATA "CreatorBrain\venv"
$vpy = Join-Path $venv "Scripts\python.exe"
New-Item -ItemType Directory -Force -Path $Work | Out-Null
Start-Transcript -Path (Join-Path $Work ("run-" + (Get-Date -Format "yyyyMMdd-HHmmss") + ".log")) | Out-Null
function Have($c) { [bool](Get-Command $c -ErrorAction SilentlyContinue) }
try {
  if (-not (Have "ffmpeg")) { throw "ffmpeg missing: run Extract-CreatorBrain.ps1 once (it installs everything) or: winget install Gyan.FFmpeg" }
  if (-not (Test-Path $vpy)) { if (Have "py") { py -3 -m venv $venv } else { python -m venv $venv } }
  if (-not $SkipInstall) {
    & $vpy -m pip install --quiet --upgrade pip
    & $vpy -m pip install --quiet --upgrade yt-dlp faster-whisper pillow numpy
    if (-not (Have "deno") -and -not (Have "node")) {
      Write-Host "Installing Deno (YouTube downloads need a JavaScript runtime)..." -ForegroundColor Cyan
      winget install --id DenoLand.Deno -e --accept-source-agreements --accept-package-agreements | Out-Host
      $env:Path = [Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [Environment]::GetEnvironmentVariable("Path", "User")
    }
  }
  if (-not (Have "claude")) { throw "Claude Code CLI missing: npm install -g @anthropic-ai/claude-code, then run 'claude' once to sign in." }
  $env:PYTHONUTF8 = "1"
  $env:Path = (Join-Path $venv "Scripts") + ";" + $env:Path   # so yt-dlp from the venv is found

  if (-not $Creators) {
    $Creators = Join-Path $Work "creators.json"
    $a = @($py, "creators", "--out", $Creators); if ($Batch) { $a += @("--batch", $Batch) }
    & $vpy @a
    Write-Host "Edit $Creators to paste exact video URLs per creator (best results), then re-run with -Creators `"$Creators`"." -ForegroundColor DarkGray
  }
  $cm = @(); if ($ClaudeModel) { $cm = @("--claude-model", $ClaudeModel) }
  if ($Steps -contains "fetch") {
    $a = @($py, "fetch", "--creators", $Creators, "--work", $Work, "--per", $Per)
    if ($Browser) { $a += @("--cookies-from-browser", $Browser) }
    & $vpy @a
  }
  if ($Steps -contains "analyse") {
    $a = @($py, "analyse", "--work", $Work, "--model", $WhisperModel) + $cm
    if ($DeleteVideos) { $a += "--delete-videos" }
    & $vpy @a
  }
  if ($Steps -contains "cards") { & $vpy $py cards --work $Work @cm }
  if ($Steps -contains "push") { & $vpy $py push --work $Work }
  Write-Host "`nDone. Cards: $Work\creators\*\card.json" -ForegroundColor Green
}
finally { Stop-Transcript | Out-Null }
