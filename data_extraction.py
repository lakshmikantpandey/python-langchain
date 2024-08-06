from langchain_community.document_loaders import UnstructuredPDFLoader
import pytesseract
# import os

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 

# Load the PDF file
pdf_path = "./pdf1.pdf"  # Replace with your PDF file path
pdf_loader = UnstructuredPDFLoader(pdf_path)

# Load documents from the PDF
documents = pdf_loader.load()

# Extract text from the loaded documents
extracted_text = "\n".join([doc.page_content for doc in documents])

# Save the extracted text to a text file
with open("extracted_data.txt", "w", encoding="utf-8") as text_file:
    text_file.write(extracted_text)

print("Data extracted and saved to extracted_data.txt")
