from langchain.vectorstores import FAISS
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain import HuggingFaceHub
from langchain.document_loaders import AzureBlobStorageContainerLoader
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter
import streamlit as st
def main():
    loader = AzureBlobStorageContainerLoader(
        conn_str="DefaultEndpointsProtocol=https;AccountName=pdfstorageaccountname;AccountKey=mfsoC2rw+oHKFYM9BgwpPj0TL2e9+idyNfiKl/Y2QWtNKxbqUWlpIDmV0W7v9ntc18UWdLyrRJec+AStGETd1Q==;EndpointSuffix=core.windows.net", 
        container="pdfcontainer")
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter (chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(docs)
    embeddings = HuggingFaceEmbeddings()
    vectordb = FAISS.from_documents(texts,embeddings)
    llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature":0,"max_length":200}, huggingfacehub_api_token="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") # type: ignore
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    pdf_qa = ConversationalRetrievalChain.from_llm(llm,vectordb.as_retriever(search_kwargs={"k": 2}), memory=memory,chain_type="stuff")
    query = st.text_input("Ask a question")
    result = pdf_qa({"question": query})["answer"]
    memory.save_context({"input": query}, {"output": result})
    # print(result)
    st.write("Answer: " + result + ".")
main()