from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter       
from langchain_openai import OpenAIEmbeddings                              
from langchain_chroma import Chroma                                       

load_dotenv()

#Loading the pdf
def index_pdf(pdf_path):
    loader = PyPDFLoader(file_path=pdf_path)
    docs = loader.load()

    #Chunking
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 400
    )
    split_docs = text_splitter.split_documents(documents=docs)

    #vector embeddings
    embedding_model = OpenAIEmbeddings(
        model = "text-embedding-3-large"
    )

    #Storing the embeddings into the DB
    vector_store = Chroma.from_documents(
        documents=split_docs,
        embedding=embedding_model,
        persist_directory="chroma_db"
    )
    print("Indexing is done...")
    

if __name__ == "__main__":
    index_pdf("test.pdf")
