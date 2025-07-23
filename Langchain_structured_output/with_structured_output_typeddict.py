from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict


load_dotenv()

model = ChatOpenAI()

#schema
class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review, method="function_calling")

result = structured_model.invoke("""I find this movie one of my childhood favourites I was only 7 to 8 yrs old when it came out used to watch it loads on video back when modern 
technology Youtube did not exist. On 100th anniversary mum and I watched it in 3d and recently watched it again together for 25th year since
it was released it even went on my own to see it again as its just so epic I just feel like I could watch it over 100 times.""")

print(result)

