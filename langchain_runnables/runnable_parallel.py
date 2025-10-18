from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template= "Generate a tweet on a {topic}",
    input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template= "Generate a linked post on a {topic}",
    input_variables= ['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
    }
)

result = parallel_chain.invoke({'topic': 'ML'})

print(result)
print(result['linkedin'])