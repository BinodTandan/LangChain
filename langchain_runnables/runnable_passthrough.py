from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}.',
    input_variables= ['topic']
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following - {text}',
    input_variables= ['text']
)

jok_seq_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
}
)

final_chain = RunnableSequence(jok_seq_chain, parallel_chain)
print(final_chain.invoke({'topic': 'AI'}))
