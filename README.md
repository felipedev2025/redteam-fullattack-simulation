# redteam-fullattack-simulation
Este projeto simula um ataque Red Team completo em um ambiente controlado, cobrindo todas as fases essenciais de um ataque real: **Reconhecimento**, **Acesso Inicial**, **Execução**, **Pós-exploração**, **Persistência** e **Exfiltração de Dados**.
# 🛡️ Red Team Full Attack Simulation

Este projeto simula um ataque Red Team completo em um ambiente controlado, cobrindo todas as fases essenciais de um ataque real: **Reconhecimento**, **Acesso Inicial**, **Execução**, **Pós-exploração**, **Persistência** e **Exfiltração de Dados**.

## 🎯 Objetivo

Demonstrar conhecimentos avançados em técnicas de pentest ofensivo e Red Teaming, utilizando ferramentas e estratégias reais, com documentação detalhada, scripts automatizados e geração de relatórios profissionais.

## 📌 Etapas do Ataque

### 1. 🔍 Reconhecimento
- Coleta de informações com `theHarvester`, `dnsrecon`, `whatweb`, `nmap`
- Enumeração de diretórios com `gobuster` e análise de serviços

### 2. 🚪 Acesso Inicial
- Exploração de vulnerabilidades (ex: CVE-XXXX)
- Uso de `Metasploit`, `msfvenom`, scripts Python customizados

### 3. 🧨 Execução
- Reverse shell, payloads e sessões interativas
- Técnicas de `lateral movement` e execução remota

### 4. 🔐 Pós-Exploração
- Coleta de credenciais com `mimikatz`
- Escalonamento de privilégios com `winPEAS` / `linPEAS`
- Análise gráfica de domínio com `BloodHound`

### 5. 🛡️ Persistência
- Criação de usuários ocultos
- Serviços maliciosos e scripts persistentes

### 6. 📤 Exfiltração
- Compressão e extração de dados sensíveis
- Scripts de upload para HTTP/FTP

## 🛠️ Ferramentas Utilizadas
- Kali Linux
- Metasploit Framework
- Mimikatz
- BloodHound
- CrackMapExec
- Empire
- Python, Bash, PowerShell
- Nmap, Gobuster, dnsrecon, theHarvester

## 📄 Relatório Técnico
O diretório `docs/` contém:
- Relatório final em PDF com vulnerabilidades e recomendações
- Diagrama da arquitetura do ataque

## ⚠️ Aviso Legal
Este projeto é **exclusivamente para fins educacionais**. Nunca utilize esse conhecimento em ambientes sem autorização formal e documentada.

---

