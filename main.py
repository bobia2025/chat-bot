from fastapi import FastAPI, Query

from loader.confluence_loader import fetch_confluence_pages
from loader.jira_loader import fetch_jira_tickets
from rag.embedding import get_embeddings
from rag.retriever import build_or_load_vectorstore
from rag.qa_chain import get_qa_chain
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings


app = FastAPI()

# Préparation initiale
pages = fetch_confluence_pages()
#print('pages:',pages)
#tickets = fetch_jira_tickets()
docs = [Document(page["content"], metadata={"title": page["title"]}) for page in pages ]

#docs = load_mock_confluence("mock_confluence.json")
embeddings = get_embeddings()
vectordb = build_or_load_vectorstore(docs, embeddings)
qa = get_qa_chain(vectordb)

@app.get("/ask")
def ask(query: str = Query(..., description="Question à poser à la base de connaissance")):
    result = qa.invoke(query)
    return {"answer": result}
