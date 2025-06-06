from DataIngestion import PDF_Load

from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

def create_embeddings():
    doc = PDF_Load("Data/attention.pdf")
    embeddings = (
        OllamaEmbeddings(model="gemma2:2b")
    )
    vectorStore = FAISS.from_documents(doc, embeddings)
    vectorStore.save_local("VectorDB/index")
    
    
    
create_embeddings()