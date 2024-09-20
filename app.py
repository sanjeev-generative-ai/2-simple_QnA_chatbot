import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

def generate_response(question, engine):
    llm = OllamaLLM(model=engine)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain.invoke({'question': question})
    return answer

engine = st.selectbox("Select model", ["llama3.1", "gemma2:27b", "mistral"])
 

st.write("Ask any question")
user_input = st.text_input("You: ")

if user_input:
    response = generate_response(user_input, engine)
    st.write(response)
else:
    st.write("Please provide an input")