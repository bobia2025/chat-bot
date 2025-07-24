from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def get_qa_chain(retriever):
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever.as_retriever(),
        return_source_documents=True
    )
    return qa_chain
