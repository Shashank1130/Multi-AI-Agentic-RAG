from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain.vectorstores.faiss import FAISS
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()

# Extracting text from pdf files from a folder
def extract_text_from_pdfs(folder_path):
    pdf_texts = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, file_name)

            try:
                loader = PyPDFLoader(file_path=pdf_path)
                docs = loader.load()
                pdf_texts.extend(docs)
            except Exception as e:
                print(f"Error processing {file_name}: {e}")
    
    return pdf_texts

# Processing, chunking, embedding and saving it in vectorstores
def process_pdfs(folder_path, chunk_size=1000, chunk_overlap=200, embedding_model="text-embedding-3-large"):
    # Extract text from PDFs
    documents = extract_text_from_pdfs(folder_path)

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap
    )

    chunks = text_splitter.split_documents(documents)
    print(len(chunks))

    # Initialize OpenAI embeddings
    embedding = OpenAIEmbeddings(model=embedding_model)

    # Create FAISS vector store
    vector_store = FAISS.from_documents(chunks, embedding)

    # Save FAISS index locally
    vector_store.save_local(r"D:\End To End RAG (2.0)\DEMO\2-vector_dbs\railways")
    print("Embedding and FAISS indexing done!")

# Finance DB
# folder_path = r"your_folder_path_for_finance_files"
# process_pdfs(folder_path=folder_path)

# Agriculture DB
# folder_path = r"your_folder_path_for_agriculture_files"
# process_pdfs(folder_path=folder_path)

# Defence DB
# folder_path = r"your_folder_path_for_defence_files"
# process_pdfs(folder_path=folder_path)

# Railways DB
# folder_path = r"your_folder_path_for_railways_files"
# process_pdfs(folder_path=folder_path)










