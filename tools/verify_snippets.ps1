# Compiles the C++ examples of this documentation against the real Voltweave headers.
#
# The examples in snippets/ are the exact files that the pages include. They are copied into a temporary folder of the
# product's development test module (so UnrealHeaderTool and the compiler see them like real game code), the project is
# built, and the temporary files are removed again. The product repository is left unchanged.
#
# Usage: powershell -ExecutionPolicy Bypass -File tools\verify_snippets.ps1 -ProductRepo "<path to the Voltweave development repository>"
# The Unreal Editor must be closed.
param(
    [Parameter(Mandatory = $true)][string]$ProductRepo,
    [string]$Engine = "C:\Program Files\Epic Games\UE_5.8"
)

$ErrorActionPreference = "Stop"
$docsRepo = Split-Path -Parent $PSScriptRoot
$target = Join-Path $ProductRepo "Plugins\VoltweaveTests\Source\VoltweaveTests\Private\DocSnippets"
$build = Join-Path $ProductRepo "Tools\Build.ps1"
if (-not (Test-Path $build)) { throw "Not a Voltweave development repository: $ProductRepo" }

if (Test-Path $target) { Remove-Item -LiteralPath $target -Recurse -Force }
New-Item -ItemType Directory -Path $target | Out-Null
try {
    $count = 0
    foreach ($file in Get-ChildItem (Join-Path $docsRepo "snippets") -File | Where-Object { $_.Extension -in ".h", ".cpp" }) {
        $text = [System.IO.File]::ReadAllText($file.FullName).Replace("MYGAME_API", "VOLTWEAVETESTS_API")
        [System.IO.File]::WriteAllText((Join-Path $target $file.Name), $text, (New-Object System.Text.UTF8Encoding($false)))
        $count++
    }
    Write-Host "Compiling $count example files..."
    $output = & powershell -NoProfile -ExecutionPolicy Bypass -File $build -Engine $Engine 2>&1
    $output | Select-Object -Last 6 | ForEach-Object { Write-Host $_ }
    $ok = ($output | Select-String -Pattern "Result: Succeeded" -Quiet)
    $warnings = @($output | Select-String -Pattern "warning C\d+" | Where-Object { $_.Line -match "DocSnippets" })
    foreach ($w in $warnings) { Write-Host "WARNING: $($w.Line)" }
}
finally {
    if (Test-Path $target) { Remove-Item -LiteralPath $target -Recurse -Force }
}
Push-Location $ProductRepo
$dirty = git status --porcelain 2>$null
Pop-Location
if ($dirty) { Write-Host "NOTE: the product repository has changes (not caused by this script unless listed): `n$dirty" }
if (-not $ok) { Write-Host "FAILED: the examples do not compile"; exit 1 }
Write-Host "OK: all examples compile against the current Voltweave headers"
