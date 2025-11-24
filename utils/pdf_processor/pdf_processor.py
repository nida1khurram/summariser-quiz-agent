from PyPDF2 import PdfReader
from PyPDF2.errors import PdfStreamError
import re

class PDFProcessor:
    """
    A class to handle PDF processing tasks.
    """
    def __init__(self):
        """
        Initializes the PDFProcessor.
        """
        pass

    def extract_text(self, pdf_file) -> str | None:
        """
        Extracts raw text from an uploaded PDF file.
        """
        try:
            pdf_reader = PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            return text
        except PdfReaderError:
            return None

    def clean_text(self, text: str) -> str:
        """
        Cleans the extracted text.
        """
        # Replace common ligatures
        text = text.replace('ﬁ', 'fi').replace('ﬂ', 'fl')
        # Normalize whitespace (replaces multiple spaces, newlines, tabs with a single space)
        text = re.sub(r'\s+', ' ', text)
        # Strip leading/trailing whitespace
        return text.strip()
