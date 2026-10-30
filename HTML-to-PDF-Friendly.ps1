# HTML-to-PDF-Friendly.ps1
# Select an HTML file, choose an output location, and export it with Chrome or Edge.
# The browser respects the HTML file's print CSS, including @page size and margins.
#
# Run from PowerShell:
#   powershell -ExecutionPolicy Bypass -File .\HTML-to-PDF-Friendly.ps1
#
# Optional automation:
#   .\HTML-to-PDF-Friendly.ps1 -HtmlPath .\resume.html -PdfPath .\resume.pdf

[CmdletBinding()]
param(
  [string]$HtmlPath,
  [string]$PdfPath,
  [switch]$NoPrompt
)

$ErrorActionPreference = 'Stop'

Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.Application]::EnableVisualStyles()

function Show-ErrorMessage {
  param([string]$Message)
  [System.Windows.Forms.MessageBox]::Show(
    $Message,
    'HTML to PDF',
    [System.Windows.Forms.MessageBoxButtons]::OK,
    [System.Windows.Forms.MessageBoxIcon]::Error
  ) | Out-Null
}

function Find-Browser {
  $candidates = @(
    "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
    "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
    "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe",
    "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe",
    "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe",
    "$env:LOCALAPPDATA\Microsoft\Edge\Application\msedge.exe"
  )

  foreach ($candidate in $candidates) {
    if ($candidate -and (Test-Path -LiteralPath $candidate)) {
      return $candidate
    }
  }

  throw 'Google Chrome or Microsoft Edge was not found. Install one of them and run the script again.'
}

try {
  if (-not $HtmlPath) {
    $openDialog = New-Object System.Windows.Forms.OpenFileDialog
    $openDialog.Title = 'Choose the HTML file to convert'
    $openDialog.Filter = 'HTML files (*.html;*.htm)|*.html;*.htm|All files (*.*)|*.*'
    $openDialog.Multiselect = $false
    $openDialog.InitialDirectory = (Get-Location).Path

    if ($openDialog.ShowDialog() -ne [System.Windows.Forms.DialogResult]::OK) {
      return
    }

    $HtmlPath = $openDialog.FileName
  }

  $htmlFile = Get-Item -LiteralPath $HtmlPath
  if ($htmlFile.Extension -notin @('.html', '.htm')) {
    throw 'Please choose an .html or .htm file.'
  }

  if (-not $PdfPath) {
    $saveDialog = New-Object System.Windows.Forms.SaveFileDialog
    $saveDialog.Title = 'Choose where to save the PDF'
    $saveDialog.Filter = 'PDF files (*.pdf)|*.pdf|All files (*.*)|*.*'
    $saveDialog.FileName = "$($htmlFile.BaseName).pdf"
    $saveDialog.InitialDirectory = $htmlFile.DirectoryName
    $saveDialog.OverwritePrompt = $true

    if ($saveDialog.ShowDialog() -ne [System.Windows.Forms.DialogResult]::OK) {
      return
    }

    $PdfPath = $saveDialog.FileName
  }

  $pdfFile = [System.IO.Path]::GetFullPath($PdfPath)
  $pdfDirectory = Split-Path -Parent $pdfFile
  if (-not (Test-Path -LiteralPath $pdfDirectory)) {
    New-Item -ItemType Directory -Path $pdfDirectory -Force | Out-Null
  }

  $browser = Find-Browser
  $htmlUri = ([System.Uri](Get-Item -LiteralPath $htmlFile.FullName).FullName).AbsoluteUri
  $tempProfile = Join-Path ([System.IO.Path]::GetTempPath()) ("html-to-pdf-" + [guid]::NewGuid().ToString('N'))
  New-Item -ItemType Directory -Path $tempProfile -Force | Out-Null

  try {
    # A temporary browser profile prevents the export from interfering with an open browser window.
    $arguments = @(
      '--headless=new',
      '--disable-gpu',
      '--disable-extensions',
      '--no-first-run',
      '--no-sandbox',
      '--no-pdf-header-footer',
      '--allow-file-access-from-files',
      "--user-data-dir=`"$tempProfile`"",
      "--print-to-pdf=`"$pdfFile`"",
      "`"$htmlUri`""
    ) -join ' '

    $process = Start-Process -FilePath $browser -ArgumentList $arguments -WindowStyle Hidden -Wait -PassThru
    Start-Sleep -Milliseconds 300

    if (-not (Test-Path -LiteralPath $pdfFile)) {
      throw "The browser did not create a PDF. Exit code: $($process.ExitCode)"
    }

    $result = Get-Item -LiteralPath $pdfFile
    if ($result.Length -eq 0) {
      throw 'The browser created an empty PDF.'
    }
  }
  finally {
    Remove-Item -LiteralPath $tempProfile -Recurse -Force -ErrorAction SilentlyContinue
  }

  if (-not $NoPrompt) {
    $openPdf = [System.Windows.Forms.MessageBox]::Show(
      "PDF created successfully:`n`n$pdfFile`n`nOpen it now?",
      'HTML to PDF - Complete',
      [System.Windows.Forms.MessageBoxButtons]::YesNo,
      [System.Windows.Forms.MessageBoxIcon]::Information
    )

    if ($openPdf -eq [System.Windows.Forms.DialogResult]::Yes) {
      Start-Process -FilePath $pdfFile
    }
  }
}
catch {
  Show-ErrorMessage $_.Exception.Message
  exit 1
}
