# Import necessary libraries
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import json

# Function to load PDF files
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

def save_extracted_data_to_file(extracted_data, filename):
    """
    Save extracted data to a text file in JSON format.

    Args:
        extracted_data (list): List of documents or text data to save.
        filename (str): The path to the file to save the data.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(extracted_data, f, ensure_ascii=False, indent=4)
    print(f"Data saved to {filename}")

def load_extracted_data_from_file(filename):
    """
    Load extracted data from a text file.

    Args:
        filename (str): The path to the file from which to load the data.

    Returns:
        list: Loaded data.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            extracted_data = json.load(f)
        return extracted_data
    except FileNotFoundError:
        print(f"{filename} not found. Extracting data from PDF.")
        return None



# Function to download and initialize HuggingFace embeddings
def download_hugging_face_embeddings():
    """
    Initialize and return Hugging Face embeddings.

    Returns:
        HuggingFaceEmbeddings: Hugging Face embeddings object.
    """
    # Initialize the Hugging Face Embeddings model
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embeddings

# Function to split extracted data into chunks
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
    documents = [Document(page_content=doc.get("text", "")) for doc in extracted_data]
    
    # Split the documents into text chunks
    text_chunks = text_splitter.split_documents(documents)
    
    return text_chunks


# Main Execution
if __name__ == "__main__":
    # Filepath for saving and loading extracted data
    data_file = "extracted_data.json"
    pdf_directory = r"D:\Project\medical_chatbot-RAG\Data"
    extracted_data = load_pdf_file(pdf_directory)

    # Step 1: Load extracted data if it already exists
    # extracted_data = load_extracted_data_from_file(data_file)
    
    if extracted_data is None:
        # Step 2: Load PDF files from a directory if data not found
        pdf_directory = r"D:\Project\medical_chatbot-RAG\Data"
        extracted_data = load_pdf_file(pdf_directory)
        
        # Step 3: Save the loaded extracted data to a file
        save_extracted_data_to_file(extracted_data, data_file)
    
    # Step 4: Download and initialize HuggingFace embeddings
    embeddings = download_hugging_face_embeddings()
    
    # Example usage of embeddings: embedding the first 2 sentences of the first document
    if extracted_data:
        first_document = extracted_data[0]
        print(f"First document content: {first_document.get('text', 'No text found')[:200]}...")  # Print first 200 chars
        
        # Embedding query: First 2 sentences from the first document
        query_text = first_document.get("text", "")[:200]  # Get the first 200 chars (adjust to sentences if needed)
        embedding_vector = embeddings.embed_query(query_text)
        print(f"Query Embedding Vector: {embedding_vector[:5]}...")  # Display the first 5 dimensions
    else:
        print("No documents found.")
    
    # Step 5: Split the loaded data into chunks
    text_chunks = split_data_into_chunks(extracted_data)
    
    # Display the text chunks
    for i, chunk in enumerate(text_chunks):
        print(f"Chunk {i+1}: {chunk.page_content}")  # Access the text using 'page_content'
