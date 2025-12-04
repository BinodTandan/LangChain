from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

loader = TextLoader('./langchain_document_loader/football.txt', encoding = 'utf-8')

docs = loader.load()

load_dotenv()
model = ChatOpenAI()

prompt = PromptTemplate(
    template= 'Write a summary of {text}',
    input_variables= ['text']
)

parser = StrOutputParser()

chain = prompt | model | parser 

print(chain.invoke({'text': docs[0].page_content}))
