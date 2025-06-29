from fastapi import APIRouter
from app.services.llm import chat_with_model
from app.schemas.llm import ChatRequest, ChatResponse

router = APIRouter(prefix="/llm", tags=["LLM"])

@router.post("/chat_llama3.3", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest) -> ChatResponse:
    """
    Endpoint to chat with the LLM.
    Accepts a system prompt and a human prompt, and returns the model's response.
    """
    response_content = chat_with_model(request.system_prompt, request.human_prompt)
    return ChatResponse(response=response_content)
