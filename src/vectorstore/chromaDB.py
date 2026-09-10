from langchain_chroma import Chroma
from src.embedding.embeddings_model import embeddings
from src.ingestion.chunker import chunks

path = "src/vectorstore/chroma_db"

vector_store = Chroma(
    persist_directory=path,
    embedding_function=embeddings
)

ids = [
    f"{chunk.metadata['source']}_{i}"
    for i, chunk in enumerate(chunks)
]

existing_ids = vector_store.get(ids=ids)["ids"]

new_chunks = []
new_ids = []

for chunk, id in zip(chunks, ids):
    if id not in existing_ids:
        new_chunks.append(chunk)
        new_ids.append(id)

if new_chunks:
    vector_store.add_documents(
        documents=new_chunks,
        ids=new_ids
    )

print("chroma Db storage has succesfully completed")