from langchain_community.vectorstores import FAISS
from langchain.schema import Document
import os
import pickle

def build_or_load_vectorstore(docs, embeddings):
    if not docs:
        raise ValueError("La liste de documents est vide. Vérifie le chargement des fichiers.")

    try:
        vectordb = FAISS.from_documents(docs, embeddings)
        return vectordb
    except IndexError:
        raise ValueError(
            "Les embeddings retournés sont vides. Vérifie que `embeddings.embed_documents` fonctionne correctement.")

