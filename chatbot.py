import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

model_id = "gpt-3.5-turbo"
os.environ["OPENAI_API_KEY"] = "<YOUR-API-KEY-HERE>"

#function to get the raw text from the PDF
def get_text():
    text = ""
    pdf_reader = PdfReader("./Base.pdf")
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

#function to split the raw text into smaller chunks for it to be processed by the model
def get_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len,
    )
    chunks = text_splitter.split_text(text)
    return chunks

#function to make the vectorstore with the chunks we divided and OpenAi's embeddings
def get_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    return vectorstore

#function to store the conversation so that the bot can remember what was said
def get_conversation(vectorstore):
    llm = ChatOpenAI(model_name = model_id, temperature=0)
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever=vectorstore.as_retriever(),
        memory = memory,
    )
    return conversation

#function to deliver the question to the bot and get the answer from it
def get_answer(user_question):
    answer = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = answer['chat_history']

    #print the chat history. if i % 2 == 0, it's the user talking. if i % 2 == 1, it's the bot talking
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            with st.chat_message("user"):
                st.markdown(message.content)
        else:
            with st.chat_message("assistant"):
                st.markdown(message.content)


#App's framework
st.set_page_config(page_title = "Chatbot Neuralmind", page_icon = "🤖", layout = "centered", initial_sidebar_state = "auto")
st.title("Chatbot sobre VU 2024 - Neuralmind")

if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = None

#main code
text = get_text()

chunks = get_chunks(text)

vectorstore = get_vectorstore(chunks)

st.session_state.conversation = get_conversation(vectorstore)

question = st.chat_input("Digite sua pergunta aqui")

if question:
    resposta = get_answer(question)