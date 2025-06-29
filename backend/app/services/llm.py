import os
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage
from app.core.config import settings


llm = ChatGroq(
    model_name=settings.GROQ_MODEL,
    temperature=0.7,
    max_tokens=1024,
)

def chat_with_model(system_prompt: str, human_prompt) -> str:
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_prompt)
    ]
    
    response = llm.invoke(messages)
    
    return response.content if response else "No response from the model."

