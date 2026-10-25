<#
.SYNOPSIS
  One-command Immich for the TITAN studio: AI-organise your photo/video library (faces, smart search, duplicates, timeline, map)
  on your own PC. Your folders are mounted READ-ONLY: Immich never moves, edits or deletes a file.

.DESCRIPTION
  1. Checks Docker Desktop (WSL2). Installs it with winget if missing (then asks you to restart Windows once).
  2. Refuses the streamed Google Drive letter (G:\) - Docker can't read it reliably. Use Drive "Mirror files" to a local folder
     (Drive for desktop -> Settings -> My Drive -> Mirror files) or copy the photo folders to a local disk first.
  3. Writes tools\immich\.env (git-ignored): random DB password, pinned Immich version, your folders as PHOTOS_1..4.
  4. Starts Immich (GPU image automatically if nvidia-smi works).
  5. Runs the studio bridge setup: admin user, best-value smart-search model, read-scoped API key (saved in
     %LOCALAPPDATA%\TitanEditor\immich.json, never in the repo), read-only external library, first scan.
  Indexing then runs in the background (roughly overnight for 10k items on CPU, much faster with an NVIDIA GPU).

.EXAMPLE
  .\Setup-Immich.ps1 -Photos "D:\Photos","D:\Phone backup" -Email you@titan.ai -DataDir "D:\ImmichData"
  (Google Photos: import the Takeout afterwards with immich-go; it lands in -DataDir, so give that a big drive)
  Then open http://localhost:2283 -> Explore -> People -> name your face "klaus" (once).
#>
[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)] [string[]] $Photos,
  [Parameter(Mandatory = $true)] [string] $Email,
  [string] $Name = "Klaus",
  [ValidateSet("auto", "cpu", "gpu", "multilingual")] [string] $Model = "auto",
  [string] $Version = "v3.3.5",
  [string] $DataDir = (Join-Path $env:LOCALAPPDATA "TitanEditor\immich-data"),   # Immich's own storage (thumbnails + anything uploaded, e.g. a Google Photos Takeout). Put it on a big drive: -DataDir "D:\ImmichData"
  [switch] $AllowStreamedDrive
)
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
function Have($c) { [bool](Get-Command $c -ErrorAction SilentlyContinue) }

if ($Photos.Count -gt 4) { throw "Up to 4 folders (add more later in Immich -> Administration -> External libraries)." }
foreach ($p in $Photos) {
  if (-not (Test-Path $p)) { throw "Folder not found: $p" }
  if (-not $AllowStreamedDrive -and $p -match '^[Gg]:\\') {
    throw "$p is on the streamed Google Drive letter. Switch Drive to 'Mirror files' (to e.g. D:\GDriveMirror) or copy the folder locally, then use that path. (-AllowStreamedDrive to try anyway.)"
  }
}

if (-not (Have "docker")) {
  Write-Host "Installing Docker Desktop (winget). Restart Windows when it finishes, open Docker Desktop once, then run this script again." -ForegroundColor Cyan
  winget install --id Docker.DockerDesktop -e --accept-source-agreements --accept-package-agreements | Out-Host
  return
}
docker info *> $null
if ($LASTEXITCODE) { throw "Docker Desktop is installed but not running. Start Docker Desktop (WSL2 backend), wait for 'Engine running', then re-run." }

$gpu = (Have "nvidia-smi") -and ((& nvidia-smi -L 2>$null) -match "GPU")
if ($Model -eq "auto") { $Model = if ($gpu) { "gpu" } else { "cpu" } }

# .env (git-ignored)
$envFile = Join-Path $here ".env"
$data = $DataDir
New-Item -ItemType Directory -Force -Path $data | Out-Null
if (-not (Test-Path $envFile)) {
  $pw = -join ((48..57) + (65..90) + (97..122) | Get-Random -Count 24 | ForEach-Object { [char]$_ })
  $lines = @("UPLOAD_LOCATION=$($data -replace '\\','/')", "DB_DATA_LOCATION=immich-pgdata", "IMMICH_VERSION=$Version", "DB_PASSWORD=$pw",
             "DB_USERNAME=postgres", "DB_DATABASE_NAME=immich")
  for ($i = 0; $i -lt $Photos.Count; $i++) { $lines += "PHOTOS_$($i + 1)=$((Resolve-Path $Photos[$i]).Path -replace '\\','/')" }
  Set-Content -Path $envFile -Value $lines -Encoding ascii
  Write-Host "Wrote $envFile" -ForegroundColor Green
} else { Write-Host "Using existing $envFile (delete it to regenerate)" -ForegroundColor Yellow }
foreach ($d in 1..4) { New-Item -ItemType Directory -Force -Path (Join-Path $here "empty$d") | Out-Null }

$files = @("-f", "docker-compose.yml", "-f", "docker-compose.override.yml")
if ($gpu) { $files += @("-f", "docker-compose.gpu.yml"); Write-Host "NVIDIA GPU found: using CUDA machine learning." -ForegroundColor Green }
Push-Location $here
try {
  docker compose @files up -d
  if ($LASTEXITCODE) { throw "docker compose failed (see output above)" }
} finally { Pop-Location }

Write-Host "Waiting for Immich to start..." -ForegroundColor Cyan
$ok = $false
for ($i = 0; $i -lt 90; $i++) {
  try { if ((Invoke-RestMethod http://localhost:2283/api/server/ping -TimeoutSec 3).res -eq "pong") { $ok = $true; break } } catch {}
  Start-Sleep 3
}
if (-not $ok) { throw "Immich did not answer on http://localhost:2283 (docker compose logs immich-server)" }

# studio bridge setup (uses the auto-editor's Python env; run tools\editor\Run-Editor.ps1 -SelfTest once if it doesn't exist)
$vpy = Join-Path $env:LOCALAPPDATA "TitanEditor\venv\Scripts\python.exe"
if (-not (Test-Path $vpy)) { $vpy = "python" }
$editor = Join-Path (Split-Path -Parent $here) "editor\editor.py"
$paths = @(); $maps = @()
for ($i = 0; $i -lt $Photos.Count; $i++) { $paths += "/mnt/photos$($i + 1)"; $maps += "/mnt/photos$($i + 1)=$((Resolve-Path $Photos[$i]).Path -replace '\\','/')" }
& $vpy $editor immich setup --email $Email --name $Name --model $Model --paths @paths --map @maps
if ($LASTEXITCODE) { throw "bridge setup failed" }
Write-Host ""
Write-Host "Done. The last line above is your Immich admin password: save it in your password manager." -ForegroundColor Green
Write-Host "Next: indexing runs in the background. In a few hours open http://localhost:2283 -> Explore -> People and name your face 'klaus'." -ForegroundColor Green
Write-Host "Studio: tools\editor\editor.py immich pick ""speaking on stage"" --person klaus --out projects\<p>\picks" -ForegroundColor Green
Start-Process "http://localhost:2283"
