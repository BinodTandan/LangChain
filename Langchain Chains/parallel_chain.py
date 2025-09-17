from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()


model1 = ChatOpenAI()

model2 = ChatOpenAI()

prompt1 = PromptTemplate(
    template = "Generate short and simple notes from the following text \n {text}",
    input_variables= ['text']
)

prompt2 = PromptTemplate(
    template = "Generate 5 short question answers from the following text \n {text}",
    input_variables= ['text']
)

prompt3 = PromptTemplate(
    template= "Merge the provided notes and quiz into a single documents \n notes -> {notes} and quiz -> {quiz}",
    input_variables= ['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

merge_chain = prompt3 | model2 | parser

chain = parallel_chain | merge_chain

text = '''
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).'''

result= chain.invoke({'text': text})

print(result)

chain.get_graph().print_ascii()
