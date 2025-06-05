# DataIngestion.py

This code is designed to load a PDF file and split its text into overlapping chunks using the `langchain_community` and `langchain_text_splitter` rexpectively. 

__PyPDFLoader:__ A loader from `Langchain` to read & extract text from PDF documents.
__RecursiveCharacterTextSplitter:__ A tool to split the entire document's content into desirable overlapping chunks.

>> Loads the PDF file from the repository.
>> Splits the PDF files into "Chunks" 
>> Chunks are stores as list of "Document object" which can be retrieved manually by simple indexing technique.