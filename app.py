import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import streamlit as st

st.set_page_config(page_title="TOCH OCR PDF", layout="wide")

st.title("TOCH OCR PDF â€“ DÃ©mo complÃ¨te")

uploaded_file = st.file_uploader("SÃ©lectionnez un fichier PDF", type="pdf")

def extract_text_from_pdf(file):
    text_output = []
    pdf_doc = fitz.open(stream=file.read(), filetype="pdf")
    for page_num in range(len(pdf_doc)):
        page = pdf_doc.load_page(page_num)
        pix = page.get_pixmap()
        img_data = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_data))
        text = pytesseract.image_to_string(image)
        text_output.append(text)
    return "\n\n".join(text_output)

if uploaded_file:
    st.info("Analyse OCR en cours...")
    extracted_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Texte extrait :")
    st.text_area("RÃ©sultat OCR", extracted_text, height=400)

    st.download_button("TÃ©lÃ©charger le texte en .txt", extracted_text, file_name="ocr_result.txt")
