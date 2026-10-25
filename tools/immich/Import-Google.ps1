<#
.SYNOPSIS
  Get your Google Drive photo folders and your Google Photos library into Immich in one command. You don't need Drive "Mirror files".

.DESCRIPTION
  -DriveFolders  copies the named folders from the streamed Drive letter (G:\My Drive\...) to a local folder (default D:\Photos\Drive)
                 with robocopy. It is resumable: run it again and it only copies what's missing. Nothing on Drive changes.
                 Then run Setup-Immich.ps1 -Photos "D:\Photos\Drive" (or add the folder later in Immich -> External libraries).
  -Takeout       imports Google Photos from Google Takeout zips with immich-go (open source; downloaded here automatically).
                 It keeps dates, albums, descriptions and GPS, and skips duplicates. Don't unzip the files.
                 You need an Immich API key with upload rights: Immich -> your avatar -> Account Settings -> API Keys -> New (all permissions).
                 The script asks for the key in a hidden prompt and never saves it.

.EXAMPLE
  .\Import-Google.ps1 -DriveFolders "G:\My Drive\Photos","G:\My Drive\Events 2024"
  .\Import-Google.ps1 -Takeout "D:\Takeout"
#>
[CmdletBinding()]
param(
  [string[]] $DriveFolders,
  [string] $DriveTo = "D:\Photos\Drive",
  [string] $Takeout,
  [string] $Server = "http://localhost:2283",
  [string] $ImmichGoVersion = "v0.32.0",
  [switch] $DryRun
)
$ErrorActionPreference = "Stop"
if (-not $DriveFolders -and -not $Takeout) { Get-Help $MyInvocation.MyCommand.Path -Detailed; return }

# 1. Google Drive folders -> local copy
foreach ($src in $DriveFolders) {
  if (-not (Test-Path $src)) { throw "Not found: $src (open File Explorer -> Google Drive (G:) -> My Drive to see the exact folder name)" }
  $dst = Join-Path $DriveTo (Split-Path $src -Leaf)
  Write-Host "Copying $src -> $dst (resumable; large folders take a while)..." -ForegroundColor Cyan
  $rc = @($src, $dst, "/E", "/MT:8", "/R:2", "/W:5", "/XO", "/NP", "/NDL")
  if ($DryRun) { $rc += "/L" }
  robocopy @rc | Select-Object -Last 12 | Out-Host
  if ($LASTEXITCODE -ge 8) { throw "robocopy reported failures (code $LASTEXITCODE). Run the same command again to retry the missing files." }
}
if ($DriveFolders) {
  Write-Host "Drive copy done: $DriveTo. Use it with Setup-Immich.ps1 -Photos ""$DriveTo"" (or Immich -> Administration -> External libraries)." -ForegroundColor Green
}

# 2. Google Photos Takeout -> Immich via immich-go
if ($Takeout) {
  $zips = @(Get-ChildItem -Path $Takeout -Filter "takeout-*.zip" -File -ErrorAction SilentlyContinue)
  if (-not $zips) { throw "No takeout-*.zip files in $Takeout. Download them from takeout.google.com first (Google Photos only, .zip, 50 GB)." }
  try { Invoke-RestMethod "$Server/api/server/ping" -TimeoutSec 5 | Out-Null } catch { throw "Immich isn't answering at $Server. Start Docker Desktop and run Setup-Immich.ps1 first." }

  $tools = Join-Path $env:LOCALAPPDATA "TitanEditor\immich-go"
  $exe = Join-Path $tools "immich-go.exe"
  if (-not (Test-Path $exe)) {
    New-Item -ItemType Directory -Force -Path $tools | Out-Null
    $arch = if ($env:PROCESSOR_ARCHITECTURE -eq "ARM64") { "arm64" } else { "x86_64" }
    $zip = Join-Path $tools "immich-go.zip"
    Write-Host "Downloading immich-go $ImmichGoVersion..." -ForegroundColor Cyan
    Invoke-WebRequest "https://github.com/simulot/immich-go/releases/download/$ImmichGoVersion/immich-go_Windows_$arch.zip" -OutFile $zip
    Expand-Archive $zip -DestinationPath $tools -Force
    Remove-Item $zip
    if (-not (Test-Path $exe)) { $found = Get-ChildItem $tools -Recurse -Filter immich-go.exe | Select-Object -First 1; if ($found) { $exe = $found.FullName } else { throw "immich-go.exe not found after download" } }
  }

  Write-Host "Found $($zips.Count) Takeout zip(s) in $Takeout." -ForegroundColor Cyan
  $sec = Read-Host "Paste your Immich UPLOAD API key (hidden, not saved)" -AsSecureString
  $key = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($sec))
  $args2 = @("upload", "from-google-photos", "--server=$Server", "--api-key=$key", "--on-errors=continue")
  if ($DryRun) { $args2 += "--dry-run" }
  $args2 += ($zips | ForEach-Object { $_.FullName })
  & $exe @args2
  $code = $LASTEXITCODE
  $key = $null
  if ($code) { throw "immich-go exited with code $code. It's safe to run again: files already uploaded are skipped." }
  Write-Host "Google Photos import done. When Immich finishes indexing, the zips in $Takeout can be deleted (your Google Photos stays untouched)." -ForegroundColor Green
}
