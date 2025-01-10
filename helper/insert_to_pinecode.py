import pinecone

from langchain.vectorstores import Pinecone
from pinecone.client.models import ServerlessSpec

from langchain.embeddings import HuggingFaceEmbeddings

def download_hugging_face_embeddings():
    """
    Initialize and return Hugging Face embeddings.

    Returns:
        HuggingFaceEmbeddings: Hugging Face embeddings object.
    """
    # Initialize the Hugging Face Embeddings model
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embeddings


def upsert_embeddings_to_pinecone(extracted_data, index_name, api_key, environment="us-west1-gcp"):
    """
    Embed the text chunks and upsert them into the Pinecone index.

    Args:
        extracted_data (list): List of text data or documents to be embedded and upserted.
        index_name (str): The name of the Pinecone index to use.
        api_key (str): The API key for Pinecone.
        environment (str): The Pinecone environment, default is "us-west1-gcp".

    Returns:
        None
    """
    # Initialize Pinecone client
    pinecone.init(api_key=api_key, environment=environment)

    # Check if index already exists
    if index_name not in pinecone.list_indexes():
        # Define the index specification (example: using serverless)
        spec = ServerlessSpec(
            cloud='aws',  # Cloud provider
            region='us-west-2'  # Cloud region
        )
        
        # Create the index with the specified dimension and spec
        pinecone.create_index(index_name, dimension=1536, spec=spec)  # Ensure the dimension matches the embedding model's output
        print(f"Index '{index_name}' created successfully.")
    else:
        print(f"Index '{index_name}' already exists, skipping creation.")

    # Convert the extracted data into documents (assuming it's already in chunks)
    documents = [{"page_content": doc["text"]} for doc in extracted_data]
    
    # Initialize the embedding model (replace with a valid method for Hugging Face embeddings if necessary)
    embeddings = download_hugging_face_embeddings()  # Replace with valid function or model
    
    # Embed and upsert into Pinecone using Pinecone
    vector_store = Pinecone.from_documents(
        documents, 
        embedding=embeddings, 
        index_name=index_name
    )

    print(f"Successfully upserted embeddings into the Pinecone index '{index_name}'.")

# Example usage:
if __name__ == "__main__":
    # Example extracted data (replace with your actual extracted data)
    extracted_data = [
        {"text": "This is a long text from a PDF file that needs to be split into chunks."},
        {"text": "Another document with a significant amount of text for splitting."}
    ]
    
    # Define your Pinecone API key and index name
    api_key = "pcsk_37Ucqa_9FgQqYi7jzTAt12tAw2DLYDAqTRiJUA4RQ5sS1sP7dV8km2yJVXiJaUR7NHoWKc"
    index_name = "medibot"
    
    # Call the function to upsert embeddings into Pinecone
    upsert_embeddings_to_pinecone(extracted_data, index_name, api_key)
