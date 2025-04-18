# TOCH OCR PDF – Flask App

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![OCR](https://img.shields.io/badge/OCR-pytesseract-green.svg)](https://github.com/madmaze/pytesseract)

## Description

**TOCH OCR PDF** est une application web développée avec Flask qui permet :

- d’uploader un fichier PDF,
- d’extraire le texte automatiquement via **OCR** (PyMuPDF + Tesseract),
- d’afficher le résultat dans une interface web,
- de télécharger le texte extrait au format `.txt` ou `.pdf`.

---

## Installation

```bash
git clone https://github.com/milyes/toch_ocr_pdf.git
cd toch_ocr_pdf
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
