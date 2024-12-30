from langchain_community.llms import Ollama
llm=Ollama(model="phi3:3.8b ")
response=llm.invoke("write a poem on rain")
print(response)