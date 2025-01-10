from pinecone import Pinecone

pc = Pinecone(api_key="pcsk_2vdwSP_33AMeyjvoa6tPyet9Wve8KcQoSPrxSYz4ixtHxmqj5wzEKsEWJDHz9T1cGGXBM2")

def create_pinecone_index(api_key, index_name, model_name, field_map, cloud="aws", region="us-east-1"):
    """
    Function to create a Pinecone index with specified parameters.
    
    Args:
        api_key (str): Pinecone API key for authentication.
        index_name (str): The name of the index to be created.
        model_name (str): The embedding model to use for vectorization.
        field_map (dict): The field map for embedding.
        cloud (str): Cloud provider (default is "aws").
        region (str): Region for Pinecone service (default is "us-east-1").
    
    Returns:
        dict: The response from the Pinecone API after creating the index.
    """
    # Initialize Pinecone with API key
    pc = Pinecone(api_key=api_key)
    
    try:
        # Create the index
        # index_model = pc.create_index_for_model(
        #     name=index_name,
        #     cloud=cloud,
        #     region=region,
        #     embed={
        #         "model": model_name,
        #         "field_map": field_map
        #     }
        # )

        index_model = pc.create_index_for_model(
            name=index_name,
            cloud="aws",
            region="us-east-1",
            embed={
            "model":"multilingual-e5-large",
            "field_map":{"text": "chunk_text"}
            }
        )
        print(f"Index '{index_name}' created successfully.")
        return index_model  # Return the index model response
    except Exception as e:
        print(f"Error creating index: {e}")
        return None

# Example usage
if __name__ == "__main__":
    api_key = "pcsk_2vdwSP_33AMeyjvoa6tPyet9Wve8KcQoSPrxSYz4ixtHxmqj5wzEKsEWJDHz9T1cGGXBM2"
    index_name = "medibot"
    model_name = "multilingual-e5-large"
    field_map = {"text": "chunk_text"}

    # Call the function to create the index
    index_model = create_pinecone_index(api_key, index_name, model_name, field_map)
    
    if index_model:
        print("Index creation response:", index_model)
