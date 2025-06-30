from pydantic import BaseModel

class ChatRequest(BaseModel):
    system_prompt: str
    human_prompt: str

class ChatResponse(BaseModel):
    response: str