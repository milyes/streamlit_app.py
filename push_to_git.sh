#!/data/data/com.termux/files/usr/bin/bash

# Script automatique pour init + push GitHub
echo "Initialisation du dépôt Git..."
git init
git add .
git commit -m 'Initial commit - TOCH OCR PDF'
git branch -M main
git remote add origin https://github.com/milyes/toch_ocr_pdf.git
git push -u origin main
