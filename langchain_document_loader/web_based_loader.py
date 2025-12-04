from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

url = "https://www.ibm.com/think/topics/variational-autoencoder"

web = WebBaseLoader(url)
docs = web.load()
load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template="Write a summary of {length} words of following \n {text}",
    input_variables= ['length', 'text']
)

parser = StrOutputParser()

chain = prompt | model | parser
print(chain.invoke({'length': 300, 'text': docs[0].page_content})) 