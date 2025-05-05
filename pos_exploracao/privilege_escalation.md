# 🧬 Escalonamento de Privilégios

Após o acesso ao sistema, realizamos a escalada de privilégios utilizando ferramentas e técnicas de enumeração.

---

## 🔍 1. Ferramentas usadas:
- winPEAS (Windows)
- linPEAS (Linux)
- manual: `whoami`, `hostname`, `net user`, `schtasks`, `wmic`

---

## 📌 2. Comandos úteis (Windows)

```cmd
whoami /priv
net localgroup administrators
dir /a c:systeminfo
tasklist /v
```

## 📌 3. Comandos úteis (Linux)

```bash
sudo -l
find / -perm -4000 2>/dev/null
uname -a
cat /etc/passwd
```

## 📈 4. Técnicas comuns

- Exploração de binários SUID
- Serviço vulnerável como SYSTEM
- Scheduled tasks
- DLL Hijacking
- Kernel exploits (Linux)

---

Documentar o vetor usado é essencial para o relatório final.

