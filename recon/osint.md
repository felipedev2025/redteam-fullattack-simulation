# 🕵️ Reconhecimento (OSINT e Enumeração)

Nesta fase, coletamos o máximo de informações possíveis sobre o alvo **antes de qualquer ataque ativo**. A ideia é mapear domínios, IPs, e-mails, tecnologia usada e possíveis superfícies de ataque.

---

## 🔎 1. Coleta com TheHarvester

```bash
theHarvester -d dominioalvo.com -b all -f resultado_harvester.html
```

> Coleta e-mails, hosts e subdomínios em motores como Google, Bing, Yahoo, etc.

---

## 🌐 2. Verificação de DNS com dnsrecon

```bash
dnsrecon -d dominioalvo.com -a
```

> Realiza brute force em subdomínios e enumeração de registros (A, MX, TXT, NS).

---

## 🛰️ 3. Scan de Portas com Nmap

```bash
nmap -sC -sV -T4 -Pn -oN nmap_scan.txt TARGET_IP
```

Parâmetros importantes:
- `-sC`: scripts padrão
- `-sV`: detecção de versões
- `-T4`: velocidade
- `-Pn`: ignora ping
- `-oN`: output no formato legível

---

## 📁 4. Enumeração de Diretórios com Gobuster

```bash
gobuster dir -u http://dominioalvo.com -w /usr/share/wordlists/dirb/common.txt -t 30
```

> Testa diretórios ocultos com wordlists.

---

## ⚙️ 5. Identificação de Tecnologias com WhatWeb

```bash
whatweb http://dominioalvo.com
```

> Detecta frameworks, CMS (WordPress, Joomla), servidores (Apache, Nginx), linguagens (PHP, ASP.NET).

---

## 🗒️ Conclusão

As informações obtidas nessa etapa são usadas para escolher a melhor forma de ataque nas fases seguintes: exploit e execução.

Sempre documente tudo para seu relatório final!
