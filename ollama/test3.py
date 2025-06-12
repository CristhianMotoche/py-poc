# Extract embeddings from text

import os
import sys
from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

file = "data/avatar_the_last_air_bender_the_art_of_the_animated_series.txt"
data = open(file, "r").read().strip().replace("\n", " ")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_text(data)

print(f"Number of chunks: {len(chunks)}")
print(f"First chunk: {chunks[0]}")
