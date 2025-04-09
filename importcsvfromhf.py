import pandas as pd

# Login using e.g. `huggingface-cli login` to access this dataset
df = pd.read_csv("hf://datasets/MarcoM003/TV-Shows-Netflix-Disney/tv-shows.csv")

df.to_csv("D:\AI ENGINEER\OllamaChatbot\movies.csv", index=False)

print(df.head())



