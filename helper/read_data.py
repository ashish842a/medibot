# Extract Data From the PDF File
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


if __name__ == "__main__":
    pdf_directory = r"D:\Project\medical_chatbot-RAG\Data"
    documents = load_pdf_file(pdf_directory)
    print(f"Loaded {len(documents)} documents.")
    print("document first page ",documents[0])
