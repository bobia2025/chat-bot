# 🤖 ChatBot IA - Assistant Confluence/Jira avec RAG

Ce projet est une application de chatbot IA en Python, basée sur **Streamlit** et **LangChain**, permettant de poser des questions en langage naturel sur des documents internes (mock ou Confluence réel). Il utilise une architecture RAG (Retrieval-Augmented Generation) avec `OpenAI GPT-4o` ou tout autre LLM compatible.

---

## 🚀 Fonctionnalités

- 🔍 Posez des questions en français sur vos documents internes
- 📄 Obtenez des réponses avec les sources documentaires citées
- 🧠 Pipeline RAG (LangChain + FAISS + OpenAI)
- 💬 Interface utilisateur simple avec **Streamlit**
- 🧪 Données mockées ou connexion réelle à **Confluence/Jira**

---

## 🧰 Stack utilisée

- [Streamlit](https://streamlit.io/) – Interface Web
- [LangChain](https://www.langchain.com/) – Chaîne RAG
- [FAISS](https://github.com/facebookresearch/faiss) – Vector Store
- [OpenAI](https://platform.openai.com/) – Modèle de génération (GPT-4o)
- [Slack API / REST Confluence API](https://developer.atlassian.com/) – En option

---

## 📦 Installation

1. **Clone le dépôt**

```bash
git clone https://github.com/bobia2025/chat-bot.git
cd chat-bot
