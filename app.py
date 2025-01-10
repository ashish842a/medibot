# Import necessary libraries
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import json

from pinecone import Pinecone
from helper.insert_to_pinecode import upsert_vectors_to_pinecone

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
    # Ensure extracted_data is a list
    if not isinstance(extracted_data, list):
        print("Error: extracted_data is not a list.")
        return

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(extracted_data, f, ensure_ascii=False, indent=4)
    print(f"Data saved to {filename}")


def load_extracted_data_from_file(filename):
    """
    Load extracted data from a JSON file.

    Args:
        filename (str): The path to the file from which to load the data.

    Returns:
        list: Loaded data as a list of dictionaries, or None if the file is not found.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            extracted_data = json.load(f)  # Load JSON content into a Python list or dictionary
        return extracted_data
    except FileNotFoundError:
        print(f"{filename} not found. Extracting data from PDF.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {filename}: {e}")
        return None


# Function to download and initialize HuggingFace embeddings
def loading_hugging_face_embeddings():
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
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    
    # Convert each dictionary into a Document object
    documents = [Document(page_content=doc.get("text", "")) for doc in extracted_data]
    
    # Split the documents into text chunks
    text_chunks = text_splitter.split_documents(documents)
    
    return text_chunks


# Main Execution
if __name__ == "__main__":
    # Filepath for saving and loading extracted data
    data_file = "medibook_content.json"
    
    extracted_data = load_extracted_data_from_file(data_file)
    
    
    
    # Step 4: Split the loaded data into chunks
    text_chunks = split_data_into_chunks(extracted_data)
    
    print("text_chunks",len(text_chunks))
    # print("text_chunks",type(text_chunks))
    # print("text_chunks",text_chunks[0])
    
    # # Extract and convert Document objects into dictionaries
    # first_chunk_data = {"text": text_chunks[0].page_content}  
    # second_chunk_data = {"text": text_chunks[1].page_content}

    # # Save first two chunks as JSON
    # with open('first_chunk.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(first_chunk_data, json_file, ensure_ascii=False, indent=4)
    #     json.dump(second_chunk_data, json_file, ensure_ascii=False, indent=4)

    # embeddings = loading_hugging_face_embeddings()
    
    # text_chunks_embedded_vector = []
    # for query in text_chunks[:3]:
    #     # print("query",query)
    #     embedding_vector = embeddings.embed_query(query.page_content)
    #     text_chunks_embedded_vector.append(embedding_vector)
        
    # print("len",len(text_chunks_embedded_vector))
    # print("vectre len",len(text_chunks_embedded_vector[0]))
        
    # api_key = "pcsk_2vdwSP_33AMeyjvoa6tPyet9Wve8KcQoSPrxSYz4ixtHxmqj5wzEKsEWJDHz9T1cGGXBM2"
    # pc = Pinecone(api_key=api_key)
    # # index = None  # Replace with your actual Pinecone index instance
    # index = pc.Index("medibot")  
    # namespace="ns1"
    # upsert_response = upsert_vectors_to_pinecone(index, text_chunks_embedded_vector, namespace)
    
      
    # print("embedded data",len(text_chunks_embedded_vector))     
    # print("embedded data1",((text_chunks_embedded_vector[0][0])))     
    # print("embedded data2",(text_chunks_embedded_vector[1][0]))     
   
        
    
