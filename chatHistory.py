from dotenv import load_dotenv
import os

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import OpenAI
from langchain.prompts.prompt import PromptTemplate

# Setup
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0)

# Templates
template = """The following is a friendly conversation between a human and an AI. The AI uses simple language and is straight to the point. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
{history}
Human: {input}
AI Assistant:"""

PROMPT = PromptTemplate(input_variables=["history", "input"], template=template)

# Conversation Chain
conversation = ConversationChain(
    prompt=PROMPT,
    llm=llm,
    verbose=True,
    memory=ConversationBufferMemory(ai_prefix="AI Assistant"),
)

while(True):
    user_input = input()

    result = conversation.predict(input=user_input)
    print(result)