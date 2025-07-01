# Survey 4 Dummies

This project scrapes a website given a URL, generates a database of embeddings using Ollama, and creates a survey based on the website content. It uses Python, devenv for environment management, and aims for type safety.

## Features
- Website scraping
- Embedding generation with Ollama
- Survey creation from content
- Type-safe Python code

## Setup
1. Ensure [Ollama](https://ollama.com/) is installed and running.
2. Clone this repository.
3. Set up the Python environment (a `.venv` is already configured).
4. Install dependencies:
   ```fish
   source .venv/bin/activate.fish
   pip install -r requirements.txt
   ```
5. Run the main script:
   ```fish
   /home/camm/code/py-poc/survey-4-dummies/.venv/bin/python main.py
   ```

## Usage
- Update `main.py` to specify the target URL.
- The script will scrape the site, generate embeddings, and output a survey.

## Notes
- Type checking: `mypy .`
- Linting: `ruff .`
- Ollama must be running locally for embedding generation.
