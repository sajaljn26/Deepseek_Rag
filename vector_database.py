from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS



pdfs_directory = 'pdfs/'
#step 1 load pdf ->
def upload_file(file):
    with open(pdfs_directory + file.name, 'wb') as f:
        f.write(file.getbuffer())

def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    return documents    

file_path = 'eng.pdf'
documents = load_pdf(file_path)

#step 2 -> Create Chunks 
def create_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        add_start_index = True  
    )
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks    

text_chunks = create_chunks(documents)
#print(len(text_chunks))

# step 3 -> Create Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# step 4 -> Create Vector Databasesss
FAISS_DB_PATH = "vectorstore/db_faiss"
faiss_db = FAISS.from_documents(text_chunks, embeddings)
faiss_db.save_local(FAISS_DB_PATH)