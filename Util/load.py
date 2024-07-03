# Util/load.py
import pandas as pd
import fitz  # PyMuPDF
import requests
from io import BytesIO
import os
import re

def loadExcel(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Check if the required columns exist
    if 'Title' not in df.columns or 'Link' not in df.columns:
        raise ValueError("Excel file must contain 'Title' and 'Link' columns")
    
    # Convert the DataFrame to a list of lists
    data = df.values.tolist()

    abstracts = []
    for title, link in data:
        try:
            # Download the PDF file
            response = requests.get(link)
            response.raise_for_status()  # Raise an exception for HTTP errors

            # Open the PDF file from the downloaded content
            pdf_document = fitz.open(stream=BytesIO(response.content), filetype="pdf")
            
            # Extract text from the first page of the PDF
            text = extract_text_from_pages(pdf_document, 1)

            # Extract the abstract or fallback to first page
            abstract = extract_abstract(text)
            abstracts.append([title, abstract])
        except Exception as e:
            print(f"Failed to process {link}: {e}")
            abstracts.append([title, "Error extracting abstract"])

    return abstracts

def loadFromFolder(folder_path):
    abstracts = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            try:
                # Open the PDF file
                pdf_document = fitz.open(file_path)
                
                # Extract text from the first page of the PDF
                text = extract_text_from_pages(pdf_document, 1)

                # Extract the abstract or fallback to first page
                abstract = extract_abstract(text)

                # Use the filename (without extension) as the title
                title = os.path.splitext(filename)[0]
                abstracts.append([title, abstract])
            except Exception as e:
                print(f"Failed to process {file_path}: {e}")
                abstracts.append([filename, "Error extracting abstract"])

    return abstracts

def extract_text_from_pages(pdf_document, num_pages):
    text = ""
    for page_num in range(min(num_pages, len(pdf_document))):
        page = pdf_document.load_page(page_num)
        text += page.get_text("text")
    return text

def extract_abstract(text):
    # Normalize text to lower case for comparison
    text_lower = text.lower()
    
    # Find the position of the phrase 'abstract:'
    abstract_start = re.search(r'\babstract:', text_lower)
    
    if abstract_start:
        # Start extracting from the position of 'abstract:'
        text_after_abstract = text[abstract_start.end():]
        
        # Find the position of the word 'introduction' or its variants
        intro_start = re.search(r'\bintro|introduction\b', text_after_abstract, re.IGNORECASE)
        
        if intro_start:
            # Extract the text before 'introduction'
            abstract = text_after_abstract[:intro_start.start()].strip()
        else:
            # If 'introduction' is not found, take all the text after 'abstract:'
            abstract = text_after_abstract.strip()
    else:
        # If 'abstract:' is not found, fallback to the first page of text
        abstract = text.strip()

    return abstract
