import requests
from bs4 import BeautifulSoup
import ollama


def scrape_website(url: str) -> str:
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return soup.get_text().strip()

def split_by_n(seq, n):
    '''A generator to divide a sequence into chunks of n units.'''
    while seq:
        yield seq[:n]
        seq = seq[n:]

def main():
    url = "https://blog.edward-li.com/tech/comparing-pyrefly-vs-ty/"  # Replace with your target URL
    client = ollama.Client()
    content = scrape_website(url)
    for chunk in split_by_n(content, 4000):
        input("Press Enter to continue...")
        print("Chunk:", chunk)
        answer = client.generate(
            model="llama3.2",
            prompt=f"""Generate 5 multiple option questions and their responses based on the following content: {chunk}""",
            options={
                "temperature": 0.1,
                "num_ctx": 4096,
            }
        )
        input("Press Enter to continue...")
        print("Response:", answer.response)


if __name__ == "__main__":
    main()
