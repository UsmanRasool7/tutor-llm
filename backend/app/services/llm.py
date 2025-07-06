from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage
from app.core.config import settings


llm = ChatGroq(
    model_name=settings.GROQ_MODEL,
    temperature=settings.GROQ_TEMPERATURE,
    max_tokens=settings.GROQ_MAX_TOKENS,
    api_key=settings.GROQ_API_KEY,               
    # If `api_key` isn’t accepted directly, use:
    # client_kwargs={"api_key": settings.GROQ_API_KEY},
)

def chat_with_model(system_prompt: str, human_prompt: str) -> str:
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_prompt)
    ]
    response = llm.invoke(messages)
    return response.content if response else "No response from the model."
