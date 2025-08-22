from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature= 0.4, max_completion_tokens=20)

result = model.invoke("Write a poem of 2  lines on football")

print(result.content)