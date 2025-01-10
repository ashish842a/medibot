from pinecone import Pinecone

def upsert_vectors_to_pinecone(index, vectors, namespace="default"):
    """
    Function to upsert vectors into a Pinecone index.

    Args:
        index (PineconeIndex): Initialized Pinecone index object.
        vectors (list): List of vectors with "id", "values", and "metadata".
        namespace (str): Optional namespace for the vectors (default is "default").
        
    Returns:
        dict: The response from Pinecone after the upsert operation.
    """
    try:
        # Ensure the vectors are 384-dimensional (you need to replace these with real 384D vectors)
        for vector,index in vectors:
            if len(vector[index]) != 384:
                print(f"Vector {vector['id']} has incorrect dimension: {len(vector[index])}. It should be 384.")
                return None
        
        # Perform the upsert operation
        response = index.upsert(
            vectors=vectors,
            namespace=namespace
        )
        print(f"Upsert operation successful. Response: {response}")
        return response  # Return the response from Pinecone after the upsert
    except Exception as e:
        print(f"Error during upsert: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Assuming the 'index' has been initialized before
    api_key = "pcsk_2vdwSP_33AMeyjvoa6tPyet9Wve8KcQoSPrxSYz4ixtHxmqj5wzEKsEWJDHz9T1cGGXBM2"
    pc = Pinecone(api_key=api_key)
    # index = None  # Replace with your actual Pinecone index instance
    index = pc.Index("medibot2")

    # Example vector data to upsert
    vectors = [
        {"id": "vec1", "values": [0.1] * 384, "metadata": {"genre": "drama"}},
        {"id": "vec2", "values": [0.2] * 384, "metadata": {"genre": "action"}},
        {"id": "vec3", "values": [0.3] * 384, "metadata": {"genre": "drama"}},
        {"id": "vec4", "values": [0.4] * 384, "metadata": {"genre": "action"}}
    ]
    
    namespace = "ns1"  # Specify the namespace
    
    # Call the function to upsert vectors
    upsert_response = upsert_vectors_to_pinecone(index, vectors, namespace)
    
    if upsert_response:
        print("Upsert successful!")
    else:
        print("Upsert failed.")
