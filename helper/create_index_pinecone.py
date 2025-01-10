import time
from pinecone import Pinecone

# Initialize Pinecone with your API key
# api_key = "pcsk_kGPAz_JyCUHoq3mC5EzZ31JLLot3hXajGtZQQqN4VwGGWnd8B8LTZCMwio7jYdZR7ePC2"
api_key = "pcsk_37Ucqa_9FgQqYi7jzTAt12tAw2DLYDAqTRiJUA4RQ5sS1sP7dV8km2yJVXiJaUR7NHoWKc"
pc = Pinecone(api_key=api_key)

# Set index name
index_name = "medibot"

# Create the index for a specific model
try:
    index_model = pc.create_index_for_model(
        name=index_name,
        cloud="aws",
        region="us-east-1",
        embed={
            "model": "multilingual-e5-large",  # Specify the embedding model to use
            "field_map": {"text": "chunk_text"}  # Map the field "chunk_text" for embedding
        }
    )
    print("Index Created:", index_model)

except Exception as e:
    print(f"Error creating index: {e}")
