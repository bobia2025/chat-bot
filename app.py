import streamlit as st
from dotenv import load_dotenv
from rag.embedding import get_embeddings
from rag.retriever import build_or_load_vectorstore
from rag.qa_chain import get_qa_chain
from loader.confluence_loader import fetch_confluence_pages
from loader.jira_loader import fetch_jira_tickets
from rag.embedding import get_embeddings
from rag.retriever import build_or_load_vectorstore
from rag.qa_chain import get_qa_chain
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
#from rag.mock_loader import load_mock_confluence  # ou loader réel

load_dotenv()

# Initialisation
st.set_page_config(page_title="Assistant Confluence", page_icon="📚")
st.title("📚 Assistant IA - Confluence RAG")

# Chargement initial des documents et du modèle
@st.cache_resource
def init_chatbot():
    #docs = load_mock_confluence("mock_confluence.json")  # ou fetch_confluence_pages()
    # Préparation initiale
    pages = fetch_confluence_pages()
    # print('pages:',pages)
    # tickets = fetch_jira_tickets()
    docs = [Document(page["content"], metadata={"title": page["title"]}) for page in pages]

    # docs = load_mock_confluence("mock_confluence.json")
    embeddings = get_embeddings()
    vectordb = build_or_load_vectorstore(docs, embeddings)
    qa = get_qa_chain(vectordb)
    return qa

qa = init_chatbot()

# État de session
if "history" not in st.session_state:
    st.session_state.history = []

# Entrée utilisateur
user_query = st.chat_input("Posez votre question...")
if user_query:
    with st.spinner("Réflexion en cours..."):
        try:
            output = qa.invoke({"query": user_query})
            response = output["result"]
            sources = [doc.metadata.get("title", "Sans titre") for doc in output["source_documents"]]
            formatted_sources = "\n".join(f"• {src}" for src in sources)
            full_response = f"**Réponse :** {response}\n\n📄 **Sources :**\n{formatted_sources}"
        except Exception as e:
            full_response = f"❌ Erreur : {str(e)}"

        st.session_state.history.append((user_query, full_response))

# Affichage de l'historique
for q, r in reversed(st.session_state.history):
    with st.chat_message("user"):
        st.markdown(q)
    with st.chat_message("assistant"):
        st.markdown(r)
