from dotenv import load_dotenv
import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv("/Users/binodtandan/Projects/personal/langchain/LangChain/.env")
hf_token = os.environ["HUGGINGFACEHUB_API_TOKEN"]

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",  
    task="text-generation",
    max_new_tokens=64,
    temperature=0.7,
    huggingfacehub_api_token=hf_token,
)

chat = ChatHuggingFace(llm=llm)
resp = chat.invoke("What is the capital of Nepal?")
print(resp.content)

