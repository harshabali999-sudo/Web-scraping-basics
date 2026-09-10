import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
# we are using the groq llm
llm = ChatGroq(
    model = "openai/gpt-oss-120b"
)