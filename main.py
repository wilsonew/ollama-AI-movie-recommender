from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are an expert in the movies field. You are given a description of what i want to see 
and you will generate a list of 5 movies that you think are similar to what i want to see.

here are some relevant movies:
{relevant_movies}

Description: {description}

List of Movies:
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    print("Welcome to the movie recommender!")
    print("\n\n-------------(q to quit)---------------------")

    question = input("What kind of movie do you want to watch today?: ")
    print("\n\n-----------------------------------------------")
    
    if question == "q":
        print("Thank you for using the movie recommender!")
        break

    movies = retriever.invoke(question)
    result = chain.invoke({"description": question, "relevant_movies": movies}) 
    print(result)






