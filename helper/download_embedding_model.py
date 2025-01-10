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


if __name__ == "__main__":
    # Download and initialize embeddings
    embeddings = download_hugging_face_embeddings()
    
    # Example usage
    query = "What is the capital of ashish?"
    embedding_vector = embeddings.embed_query(query)
    
    print(f"Query Embedding Vector: {embedding_vector[:5]}...")  # Display the first 5 dimensions
