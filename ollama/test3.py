# Extract embeddings from text

import os
import sys
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.chat_models import ChatOllama
import ollama
from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.retrievers.multi_query import MultiQueryRetriever

# GET DATA

file = "data/avatar_the_last_air_bender_the_art_of_the_animated_series.txt"
data = open(file, "r").read().strip().replace("\n", " ")

print("[INFO] Data loaded successfully.")

# GET CHUNKS

text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200, chunk_overlap=300
)
chunks = text_splitter.split_text(data)
# for i, chunk in enumerate(chunks):
#     print(f"Chunk {i+1}: {chunk}...")  # Print first 50 characters of each chunk
# sys.exit(0)

print("[INFO] Text split into chunks successfully.")

# print(f"Number of chunks: {len(chunks)}")
# print(f"First chunk: {chunks[0]}")

# BUILD VECTOR DATABASE

ollama.pull("nomic-embed-text")

vector_db = Chroma.from_texts(
    texts=chunks,
    embedding=OllamaEmbeddings(model="nomic-embed-text"),
    persist_directory="db",
)

print("[INFO] Vector database created successfully.")

# RETRIEVAL

llm = ChatOllama(model="llama3.2")
query_prompt = PromptTemplate(
    input_variables=["question"],
    template="""You are an assistant that knows about Avatar: The Last Airbender.
    Question: {question}""",
)

retriever = MultiQueryRetriever.from_llm(
    vector_db.as_retriever(),
    llm,
    prompt=query_prompt,
)

print("[INFO] Retriever created successfully.")

# RAG PROMPT

template = """Answer the question based ONLY on the context provided.
Context: {context}
Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

chain = (
    { "context": retriever, "question": RunnablePassthrough() }
    | prompt
    | llm
    | StrOutputParser()
)

print("[INFO] RAG chain created successfully.")

# RUN CHAIN
# q = "What is the document about?"
q = "What was the first thoughts of Bryan Konietzko for Momo? Who was Momo-3?"
result = chain.invoke({"query": q})
print(f"Question: {q}", result)
