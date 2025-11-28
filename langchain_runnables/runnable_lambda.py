from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Write a joke about {topic}.',
    input_variables= ['topic']
)

parser = StrOutputParser()


jok_seq_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word': RunnableLambda(lambda x: len(x.split()))
}
)

final_chain = RunnableSequence(jok_seq_chain, parallel_chain)

print(final_chain.invoke({'topic': "AI"}))
