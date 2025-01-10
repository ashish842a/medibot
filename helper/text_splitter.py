from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

def split_data_into_chunks(extracted_data):
    """
    Split extracted data into manageable text chunks.

    Args:
        extracted_data (list): List of documents or text data.

    Returns:
        list: A list of text chunks.
    """
    # Initialize the text splitter with a specific chunk size and overlap
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    
    # Convert each dictionary into a Document object
    documents = [Document(page_content=doc["text"]) for doc in extracted_data]
   
    
    # Split the documents into text chunks
    text_chunks = text_splitter.split_documents(documents)
    
    return text_chunks

if __name__ == "__main__":
    # Example extracted data (replace with actual extracted data)
    extracted_data = [
        {"text": "This is a long text from a PDF file that needs to be split into chunks."},
        {"text": "Another document with a significant amount of text for splitting."}
    ]
    
    # Split the data into chunks
    text_chunks = split_data_into_chunks(extracted_data)

    print("tyep",type(text_chunks))
    
    # Display the text chunks
    for i, chunk in enumerate(text_chunks):
        print(f"Chunk {i+1}: {chunk.page_content}")  # Access the text using 'page_content'
