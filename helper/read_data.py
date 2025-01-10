from langchain.document_loaders import DirectoryLoader

def load_pdf_file(data):
    """
    Load PDF files from the specified directory.

    Args:
        data (str): Path to the directory containing the PDF files.

    Returns:
        list: A list of document objects loaded from the PDFs.
    """
    # Initialize the DirectoryLoader for PDF files
    loader = DirectoryLoader(data, glob="*.pdf")
    
    # Load documents from the directory
    documents = loader.load()
    
    return documents

import json

if __name__ == "__main__":
    pdf_directory = r"/home/user/Github/chat_bot/medibot/Data"
    # pdf_directory = r"/home/user/Github/chat_bot/medibot/sample"
    extracted_data = load_pdf_file(pdf_directory)
    print(f"Loaded {len(extracted_data)} documents.")
    
    medibook_content = []  # Initialize an empty list to store content dictionaries

    # Save content to text file and prepare dictionary for JSON
    with open('medibook_text.txt', 'w', encoding='utf-8') as f:
        for document in extracted_data:
            page_content = document.page_content  # Access page content
            medibook_content.append({"text": page_content})  # Store content as dictionary
            f.write(page_content + "\n\n")  # Write content to the text file

    # Save the content array to a JSON file in the desired format
    with open('medibook_content.json', 'w', encoding='utf-8') as json_file:
        json.dump(medibook_content, json_file, ensure_ascii=False, indent=4)

    print("Document content saved to dictionary list, text file, and JSON file successfully.")
