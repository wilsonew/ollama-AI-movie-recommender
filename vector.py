from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

# Get the directory where this script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Use relative paths from the script's location
movies_path = os.path.join(current_dir, "movies.csv")
db_location = os.path.join(current_dir, "chrome_langchain_db")

df = pd.read_csv(movies_path)
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content=row["title"] + " " + row["description"],
            metadata={"rating": row["rating"], "genre": row["listed_in"], "platform": row["platform"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="movies",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents, ids=ids)


retriever = vector_store.as_retriever(
    search_kwargs={"k": 10}
)
