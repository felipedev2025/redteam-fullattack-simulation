from fpdf import FPDF
from datetime import datetime

# Criar o relatório técnico em PDF
class PDFRelatorio(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Relatório Técnico - Simulação Red Team", ln=True, align="C")
        self.set_font("Arial", "", 10)
        self.cell(0, 10, f"Autor: Felipe Fragoso | Data: {datetime.today().strftime('%d/%m/%Y')}", ln=True, align="C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 11)
        self.cell(0, 10, title, ln=True)
        self.set_font("Arial", "", 10)

    def chapter_body(self, body):
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDFRelatorio()
pdf.add_page()

# Títulos e conteúdos do relatório
sections = {
    "Objetivo": """Este projeto simula uma cadeia de ataque Red Team completa, com o objetivo de testar a segurança de um ambiente em camadas. Todas as fases são executadas em laboratório controlado e documentadas.""",
    "1. Reconhecimento": """Coleta de informações com ferramentas como theHarvester, dnsrecon, Nmap, Gobuster e WhatWeb para identificar superfícies de ataque e tecnologias do alvo.""",
    "2. Acesso Inicial": """Utilização de exploits públicos identificados com o Nmap + Searchsploit. Execução de ataque via Metasploit contra o serviço vsftpd 2.3.4.""",
    "3. Execução": """Geração de payload com msfvenom e captura de sessão com meterpreter usando o Metasploit multi/handler.""",
    "4. Pós-exploração": """Extração de credenciais com mimikatz, mapeamento de domínio com BloodHound, e escalonamento de privilégios com winPEAS e técnicas manuais.""",
    "5. Persistência": """Criação de usuários administrativos, serviços automatizados no Windows e backdoors em scripts de inicialização.""",
    "6. Exfiltração": """Extração de arquivos sensíveis com curl, netcat e scripts Python via HTTP POST, além de compressão com tar/gzip.""",
    "Conclusão": """Este projeto demonstrou na prática como funciona uma cadeia ofensiva completa de Red Teaming, desde a enumeração até a extração de dados, com documentação técnica e organização adequada para portfólio profissional."""
}

# Adicionar conteúdo ao PDF
for title, body in sections.items():
    pdf.chapter_title(title)
    pdf.chapter_body(body)

# Salvar o PDF
relatorio_path = "/mnt/data/relatorio_redteam_felipefragoso.pdf"
pdf.output(relatorio_path)
