from pdfminer.high_level import extract_text


text = extract_text("data/test_pdf.pdf")
print(text)
