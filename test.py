#load env by load_env
from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

llm = OpenAI()
chat_model = ChatOpenAI()

res = chat_model.predict("Hello, how are you?")

print(res)