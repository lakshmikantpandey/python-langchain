import gradio as gr
from langchain_community.document_loaders import UnstructuredPDFLoader
import pytesseract

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf(pdf_path):
    # Load the PDF file
    pdf_loader = UnstructuredPDFLoader(pdf_path)

    # Load documents from the PDF
    documents = pdf_loader.load()

    # Extract text from the loaded documents
    extracted_text = "\n".join([doc.page_content for doc in documents])

    return extracted_text

def main():
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column():
                pdf_input = gr.File(label="Upload PDF File")
                submit_button = gr.Button("Extract Text")

            with gr.Column():
                output_text = gr.Textbox(label="Extracted Text", lines=10)

        submit_button.click(
            fn=extract_text_from_pdf,
            inputs=pdf_input,
            outputs=output_text
        )

    demo.launch()

if __name__ == "__main__":
    main()
