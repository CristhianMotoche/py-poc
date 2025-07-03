from typing import List
import requests
from bs4 import BeautifulSoup
import ollama
import array

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

def scrape_website(url: str) -> str:
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return soup.get_text().strip()

def generate_embedding(text: str, client: ollama.Client) -> bytes:
    embedding = client.embeddings(model="nomic-embed-text", prompt=text)["embedding"]
    # Convert list of floats to bytes for storage
    arr = array.array('f', embedding)
    return arr.tobytes()

def create_survey(content: str, client: ollama.Client) -> str:
    """
    Generate survey questions from website content using Ollama LLM.
    Returns the raw response text.
    """
    prompt = (
        "Given the following website content, generate 5 questions. "
        f"Content:\n{content}\n"
    )
    return client.generate(model="llama3.2", prompt=prompt)["response"]

def get_retriever(data: str) -> Chroma:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200, chunk_overlap=300
    )
    chunks = text_splitter.split_text(data)

    print("[INFO] Text split into chunks successfully.")

    db = Chroma.from_texts(
        texts=chunks,
        embedding=OllamaEmbeddings(model="nomic-embed-text"),
        persist_directory="db",
    )
    return db.as_retriever()


def gen_chain(llm, retriever):
    # Create a question / answer pipeline
    rag_template = """Gegenerate 5 multiple option questions and their responses based on the following context:
    {context}
    """
    rag_prompt = ChatPromptTemplate.from_template(rag_template)
    return (
        {"context": retriever, "question": RunnablePassthrough()}
        | rag_prompt
        | llm
        | StrOutputParser()
    )



def main():
    url = "https://blog.edward-li.com/tech/comparing-pyrefly-vs-ty/"  # Replace with your target URL
    client = ChatOllama(model="llama3.2", temperature=0.1, max_tokens=1000)
    content = scrape_website(url)
    retriever = get_retriever(content)
    chain = gen_chain(client, retriever)
    print(chain.invoke(""))

if __name__ == "__main__":
    main()
