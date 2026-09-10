from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

Answer the user's question using only the provided context.

If the answer is not present in the context, say:
"I don't have enough information in the provided documents."

Do not make up or hallucinate information.

Context:
{context}

Question:
{question}

Answer:
""")