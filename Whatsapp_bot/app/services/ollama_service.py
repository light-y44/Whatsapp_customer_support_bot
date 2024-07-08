from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import asyncio
from concurrent.futures import ThreadPoolExecutor
import os

executor = ThreadPoolExecutor()

from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")



prompt = ChatPromptTemplate.from_template("""
                                          Answer the following question based on only the context provided
    Think step by step while answering.
        <context>
        {context}
        </context>
        Question: {input} """)

PATH = "/Users/devanshgupta/Desktop/WhatsApp_bot/python-whatsapp-bot/app/services/Data.pdf"

def load_documents(PATH):
    loader = PyPDFLoader(PATH)
    text_documents = loader.load()
    return text_documents


def text_splitter(text_documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
    documents = text_splitter.split_documents(text_documents)
    return documents

def create_embeddings(documents):
    embeddings = OllamaEmbeddings(model = 'nomic-embed-text')
    db = Chroma.from_documents(documents, embedding=embeddings)
    return db

def generate_answer(message_body):
    text_documents = load_documents(PATH)
    documents = text_splitter(text_documents)
    db = create_embeddings(documents)
    llm = Ollama(model = "llama2")

    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = db.as_retriever()
    retriever_chain = create_retrieval_chain(retriever, document_chain)
    response = retriever_chain.invoke({"input":message_body})
    
    return response['answer']


print(generate_answer("what are Hydrocarbons?"))





