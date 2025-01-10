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
    # pdf_directory = r"/home/user/Github/chat_bot/medibot/sample"
    pdf_directory = r"/home/user/Github/chat_bot/medibot/Data"
    
    extracted_data = load_pdf_file(pdf_directory)
    print(f"Loaded {len(extracted_data)} documents.")
    
    # with open('medibook_text.txt', 'w', encoding='utf-8') as f:
    #     for document in extracted_data:
    #         f.write(document.page_content + "\n\n")  # Write each document's content followed by two newlines
    
    medibook_content = []  # Initialize an empty list to store page contents

    dict = {}
    # Save content to text file and array
    with open('medibook_text.txt', 'w', encoding='utf-8') as f:
        for document in extracted_data:
            page_content = document.page_content  # Access page content
            dict.append({"text":page_content})
            medibook_content.append(page_content)  # Add content to the list
            f.write(page_content + "\n\n")  # Write content to the file

   
    # Save the content array to a JSON file
    with open('medibook_content.json', 'w', encoding='utf-8') as json_file:
       
        json.dump(medibook_content, json_file, ensure_ascii=False, indent=4)

    print("Document content saved to array, text file, and JSON file successfully.")
    
    # Write the first two documents' representations to a text file
    with open('medibook_text_each.txt', 'w', encoding='utf-8') as f:
        if len(extracted_data) > 0:
            f.write(repr(extracted_data[0]) + "\n\n")
        if len(extracted_data) > 1:
            f.write(repr(extracted_data[1]))
    
    # Write the content of all documents to a text file
    
    print("All documents' content saved successfully.")
