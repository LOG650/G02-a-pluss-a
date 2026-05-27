"""
Legg til sidetall i PDF-en.
Sidene før innledningen får ingen sidetall.
Fra innledningen starter nummereringen på 1/39.

Bruk:
    python3 legg_til_sidetall.py "rapport 27. mai.pdf" "rapport_med_sidetall.pdf"

Eller uten argumenter (bruker standardnavn):
    python3 legg_til_sidetall.py
"""

import sys
import os
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

FIRST_NUMBERED_PAGE = 6  # PDF-side der innledningen starter
TOTAL_NUMBERED_PAGES = 39  # Totalt antall nummererte sider

def create_page_number_overlay(page_width, page_height, display_number, total):
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(page_width, page_height))
    c.setFont("Helvetica", 9)
    c.setFillColorRGB(0.4, 0.4, 0.4)
    text = f"{display_number} / {total}"
    c.drawCentredString(page_width / 2, 30, text)
    c.save()
    packet.seek(0)
    return PdfReader(packet).pages[0]

def add_page_numbers(input_path, output_path):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for i, page in enumerate(reader.pages):
        pdf_page_num = i + 1
        if pdf_page_num >= FIRST_NUMBERED_PAGE:
            display_num = pdf_page_num - FIRST_NUMBERED_PAGE + 1
            width = float(page.mediabox.width)
            height = float(page.mediabox.height)
            overlay = create_page_number_overlay(width, height, display_num, TOTAL_NUMBERED_PAGES)
            page.merge_page(overlay)
        writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)
    print(f"Ferdig! Sidetall lagt til fra side {FIRST_NUMBERED_PAGE} (1/{TOTAL_NUMBERED_PAGES}).")
    print(f"Lagret som: {output_path}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    if len(sys.argv) >= 3:
        input_pdf = sys.argv[1]
        output_pdf = sys.argv[2]
    elif len(sys.argv) == 2:
        input_pdf = sys.argv[1]
        name, ext = os.path.splitext(input_pdf)
        output_pdf = f"{name}_med_sidetall{ext}"
    else:
        input_pdf = os.path.join(script_dir, "rapport 27. mai.pdf")
        output_pdf = os.path.join(script_dir, "rapport_med_sidetall.pdf")

    if not os.path.exists(input_pdf):
        print(f"Feil: Finner ikke filen '{input_pdf}'")
        sys.exit(1)

    add_page_numbers(input_pdf, output_pdf)
