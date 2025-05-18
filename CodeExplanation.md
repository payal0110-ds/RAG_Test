# DataIngection.py 

This Python code is designed to load and process a __PDF__ file using the langchain framework, particularly from the langchain_community and langchain_text_splitters modules.

- __PyPDFLoader:__ A loader from Langchain to read and extract text from PDF documents.
- __RecursiveCharacterTextSplitter:__ A tool to split large chunks of text into smaller, manageable parts while preserving overlap between them (useful for chunk-based processing like embedding or summarization).

- A function __PDFload__ is cretaed that takes the path to a PDF file as an input.
- __loader = PyPDFLoader(path):__ Initializes the loader with the PDF file.
- __loader.load():__ Reads the PDF and returns its content as a list of Langchain Document objects, where each object typically represents a page.

            text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
- Creates a text splitter that breaks text into chunks of 500 characters, with an overlap of 50 characters between chunks (helps preserve context across splits).
 
            text = text_splitter.split_documents(docs)
- Splits the loaded PDF documents into chunks using the defined splitter. The result is a list of smaller Document chunks, each with metadata and content.

- __return text:__ Returns the list of split document chunks.
- __result[0]__ Shows the first chunk, __result[1]__ shows the second chunk and so on. Here the index specifies each chunk.
