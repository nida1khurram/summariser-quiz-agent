# PDF Processor & File Handler

## Overview
This utility provides a robust system for processing PDF files, including text extraction, cleaning, and file handling.

## `PDFProcessor`

### **File**: `utils/pdf_processor.py`

### **Class**: `PDFProcessor`

A class to handle PDF processing tasks.

#### **Methods**

- **`__init__(self)`**
  - Initializes the PDFProcessor.

- **`extract_text(self, pdf_file: UploadedFile) -> str | None:`**
  - **Description**: Extracts raw text from an uploaded PDF file.
  - **Error Handling**: Should catch `PyPDF2.errors.PdfReaderError` and return `None` if the PDF is corrupted or unreadable.
  - **Returns**: The extracted text as a string, or `None` on failure.

- **`clean_text(self, text: str) -> str:`**
  - **Description**: Cleans the extracted text by performing the following:
    1.  Replaces common ligatures (e.g., `ﬁ`, `ﬂ`) with their standard representations (`fi`, `fl`).
    2.  Normalizes whitespace by replacing multiple spaces, newlines, and tabs with a single space.
    3.  Strips leading/trailing whitespace.
  - **Returns**: The cleaned text as a string.

## `FileHandler`

### **File**: `utils/file_handler.py`

### **Class**: `FileHandler`

A class for handling file-related operations.

#### **Methods**

- **`save_text_to_file(self, content: str, output_path: str) -> bool:`**
  - **Description**: Saves the given text content to a specified file path.
  - **Error Handling**: Should handle potential `IOError` or other file-related exceptions.
  - **Returns**: `True` on successful save, `False` otherwise.