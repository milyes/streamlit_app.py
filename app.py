from flask import Flask, render_template, request, Response
import os
from utils.ocr_engine import extract_text_from_pdf
from fpdf import FPDF

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf_file' not in request.files:
        return "Aucun fichier reçu", 400
    file = request.files['pdf_file']
    if file.filename == '':
        return "Fichier vide", 400
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    text = extract_text_from_pdf(filepath)
    return render_template('result.html', extracted_text=text)

@app.route('/export', methods=['POST'])
def export_txt():
    text = request.form.get('text_content', '')
    return Response(
        text,
        mimetype='text/plain',
        headers={'Content-Disposition': 'attachment;filename=extrait_ocr.txt'}
    )

@app.route('/export_pdf', methods=['POST'])
def export_pdf():
    text = request.form.get('text_content', '')
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in text.splitlines():
        pdf.multi_cell(0, 10, line)
    return Response(
        pdf.output(dest='S').encode('latin-1'),
        mimetype='application/pdf',
        headers={'Content-Disposition': 'attachment;filename=extrait_ocr.pdf'}
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
