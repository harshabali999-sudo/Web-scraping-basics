from src.retrival.retriever import retriever
from src.generation.prompt import prompt
from src.generation.llm import llm


def rag_pipeline(query):

    # 1. Retrieve relevant documents
    documents = retriever.invoke(query)

    # 2. Convert documents into context
    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    # 3. Create the prompt
    final_prompt = prompt.invoke({
        "context": context,
        "question": query
    })

    # 4. Send prompt to LLM
    response = llm.invoke(final_prompt)

    return response.content

# with this we have completely done the retriever side 