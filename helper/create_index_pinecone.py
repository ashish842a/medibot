import time
from pinecone import Pinecone, ServerlessSpec

# Initialize Pinecone with your API key
# api_key = "pcsk_kGPAz_JyCUHoq3mC5EzZ31JLLot3hXajGtZQQqN4VwGGWnd8B8LTZCMwio7jYdZR7ePC2"
# api_key = "pcsk_37Ucqa_9FgQqYi7jzTAt12tAw2DLYDAqTRiJUA4RQ5sS1sP7dV8km2yJVXiJaUR7NHoWKc"


api_key = "pcsk_2vdwSP_33AMeyjvoa6tPyet9Wve8KcQoSPrxSYz4ixtHxmqj5wzEKsEWJDHz9T1cGGXBM2"
pc = Pinecone(api_key=api_key)

# Set index name
index_name = "medibot2"

# Create the index for a specific model
try:
    index_model = pc.create_index(
            name=index_name,
            dimension=384, # Replace with your model dimensions
            metric="cosine", # Replace with your model metric
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            ) 
        )
    print("Index Created:", index_model)

except Exception as e:
    print(f"Error creating index: {e}")
