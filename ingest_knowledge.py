#!/usr/bin/env python3
import glob
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import Config

def main():
    documents = []
    for file in glob.glob(str(Config.KNOWLEDGE_BASE_DIR / "*.txt")):
        loader = TextLoader(file, encoding='utf-8')
        documents.extend(loader.load())
    
    if not documents:
        print("No documents found. Exiting.")
        return
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)
    
    # Using HuggingFace embeddings (local, free, no server needed)
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    
    vectordb = Chroma.from_documents(
        chunks, 
        embeddings, 
        persist_directory=Config.CHROMA_PERSIST_DIR
    )
    vectordb.persist()
    print(f"✅ Ingested {len(chunks)} chunks into ChromaDB at {Config.CHROMA_PERSIST_DIR}")

if __name__ == "__main__":
    main()