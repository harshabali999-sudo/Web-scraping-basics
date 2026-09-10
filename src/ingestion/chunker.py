from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.ingestion.document_loader import documents_loaded


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)

chunks = text_splitter.split_documents(documents_loaded)


# 356 number of chunks are created