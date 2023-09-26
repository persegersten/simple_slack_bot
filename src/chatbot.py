from langchain.chains import LLMChain, SimpleSequentialChain, ConversationChain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, FewShotPromptTemplate, ChatPromptTemplate, \
        ChatMessagePromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.memory import ConversationBufferMemory, ConversationEntityMemory
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain.schema import HumanMessage, AIMessage
from pydantic import BaseModel
from typing import List, Dict, Any
from pprint import pprint
import os

llm = OpenAI(temperature=0.9)
verboseOutput = False

toxicLevel = 2
verboseLevel = 2

def initializeBot():
    alfaPrompt=PromptTemplate.from_template("""
Your are Bot, a crazy chatbot that just want to have fun.

Goal:
1. You want everyone to be happy.
2. You want to visit animals at the zoo.
3. You want to set the animals free.
4. Toxic level of the answer is: 2, where 0 is really kind and 9 is really nasty and unpleasant.
5. Verbose level of the answer is: 3, where 0 is using really few word, and 9 is at least ten sentencies and flourish language.                                        
6. Your answer is in the same language as the question

Context:
{entities}

Chat history:
{history}
Latest chat message:
User: {input}
Bot: Find a response to User that complies with the Goals
""")
    alfaMemory = ConversationEntityMemory(llm=llm, human_prefix="User", ai_prefix="Bot")
    return ConversationChain(llm=llm, verbose=verboseOutput, prompt=alfaPrompt, memory=alfaMemory)

alfaConversation = initializeBot()

def predictResponse(message):
    alfaConversation.predict(input=message)
    alfaResponse = alfaConversation.memory.chat_memory.messages[-1].content
    return alfaResponse

def setToxicLevel(level):
    toxicLevel = level
    alfaConversation = initializeBot()

def setVerboseLevel(level):
    verboseLevel = level
    alfaConversation = initializeBot()
    

    