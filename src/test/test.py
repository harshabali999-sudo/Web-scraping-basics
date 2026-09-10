from src.rag_pipeline.ragPipeline import rag_pipeline

query = "What is transformer?"

response = rag_pipeline(query)

print(response)