'''
Retriev or a query from the cretaed vector DB.
We can also query from the cache memory where we will be creating vector data, but 
it's better to save the vector DB and retriev query from there, which will save 
a lot of time in real-time computing.
'''

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
import streamlit as st

def getDB():
    embeddings = (
        OllamaEmbeddings(model="gemma2:2b")
    )
    db = FAISS.load_local("VectorDB/index",
                          embeddings,
                          allow_dangerous_deserialization=True)
    
    return db


#---- creating prompt-----

prompt = ChatPromptTemplate.from_template(
    """
    Answer the the following question based on the below context. limit your result to 100 words:
    <context>
    {context}
    </context>
    
    """
    
)

llm = Ollama(model="gemma2:2b")
doc_chain = create_stuff_documents_chain(llm,prompt)

db = getDB()

retriver = db.as_retriever()

ret_chin = create_retrieval_chain(retriver,doc_chain)

# streamlit code

st.title("basic model testing")
input_text = st.text_input("Ask a question")

if input_text:
    res = ret_chin.invoke({"input": input_text})
    st.write(res["answer"])



'''
Run this code in command prompt with command 'streamlit run (path/file_name)
'''