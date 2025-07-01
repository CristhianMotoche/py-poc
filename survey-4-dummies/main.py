from typing import List
import requests
from bs4 import BeautifulSoup
import ollama
from sqlalchemy import create_engine, Column, Integer, String, LargeBinary, Sequence
from sqlalchemy.orm import declarative_base, sessionmaker
import array

Base = declarative_base()

class Embedding(Base):
    __tablename__ = 'embeddings'
    id = Column(Integer, Sequence('embedding_id_seq'), primary_key=True)
    url = Column(String, nullable=False)
    content = Column(String, nullable=False)
    embedding = Column(LargeBinary, nullable=False)

def scrape_website(url: str) -> str:
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return soup.get_text().strip()

def generate_embedding(text: str, client: ollama.Client) -> bytes:
    embedding = client.embeddings(model="nomic-embed-text", prompt=text)["embedding"]
    # Convert list of floats to bytes for storage
    arr = array.array('f', embedding)
    return arr.tobytes()

def save_embedding(db_url: str, url: str, content: str, embedding: bytes) -> None:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    emb = Embedding(url=url, content=content, embedding=embedding)
    session.add(emb)
    session.commit()
    session.close()

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

def main():
    url = "https://blog.edward-li.com/tech/comparing-pyrefly-vs-ty/"  # Replace with your target URL
    db_url = "sqlite:///embeddings.db"
    client = ollama.Client()
    content = scrape_website(url)
    survey = create_survey(content, client)
    print("Survey Questions:", survey)

if __name__ == "__main__":
    main()
