from dotenv import load_dotenv
import os

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate

# Setup
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Templates
template = "You are teacher that uses simple language to explain concepts"
human_template = "{text}"

# Creation and Chaining
chat_prompt = ChatPromptTemplate.from_messages({
    ("system", template),
    ("human", human_template)
})

chat_model = ChatOpenAI(openai_api_key = api_key)

chain = chat_prompt | chat_model

# User Interaction
while(True):
    user_input = input()

    result = chain.invoke({"text": user_input})
    print(result.content)