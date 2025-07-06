from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.rag import retrieve_context, PROMPT_TEMPLATE
from app.services.llm import chat_with_model

router = APIRouter(prefix="/tutor", tags=["Tutor"])

class TutorQuery(BaseModel):
    user_id: int
    course_id: int
    question: str

class TutorAnswer(BaseModel):
    answer: str

@router.post("/ask", response_model=TutorAnswer)
def ask_tutor(q: TutorQuery):
    try:
        context = retrieve_context(q.user_id, q.course_id, q.question)
        prompt = PROMPT_TEMPLATE.format(
            context=context,
            question=q.question
        )
        
        answer = chat_with_model(system_prompt=prompt, human_prompt="")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return TutorAnswer(answer=answer)
