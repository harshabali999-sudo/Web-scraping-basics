from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

def load_documents(datapath="data/raw/"):
    documents = []

    for pdf_file in Path(datapath).glob("*.pdf"):
        loader = PyMuPDFLoader(str(pdf_file))
        documents.extend(loader.load())
    return documents

documents_loaded = load_documents("data/raw/")
# all the documents are succesfully loaded