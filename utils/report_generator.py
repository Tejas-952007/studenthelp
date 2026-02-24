from __future__ import annotations

from fpdf import FPDF


def build_pdf_report(title: str, body: str, output_path: str) -> str:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Helvetica", size=16)
    pdf.multi_cell(0, 10, title)
    pdf.ln(4)
    pdf.set_font("Helvetica", size=11)
    pdf.multi_cell(0, 7, body)
    pdf.output(output_path)
    return output_path
