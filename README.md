# Ollama Movie Recommender

A movie recommendation system using Ollama and LangChain for natural language processing and vector embeddings.

## Features

- Movie recommendations based on natural language queries
- Uses Ollama for embeddings and language processing
- Vector storage with ChromaDB
- CSV-based movie database

## Requirements

- Python 3.8+
- Ollama (for running the embedding model)
- Required Python packages:
  - langchain
  - langchain-ollama
  - chromadb
  - pandas

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/ollama-movie-recommender.git
cd ollama-movie-recommender
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Pull the required Ollama model:
```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
```

## Usage

1. Place your movies.csv file in the project directory
2. Run the vector.py script to create the vector database
3. Use the main.py script to interact with the recommender

## Project Structure

- `vector.py`: Handles vector database creation and management
- `movies.csv`: Movie database (not included, add your own)
- `main.py`: Main application script 
