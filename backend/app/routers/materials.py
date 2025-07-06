from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.materials import ingest_pdf

router = APIRouter(prefix="/materials", tags=["Materials"])

@router.post("/upload_pdf")
async def upload_pdf(
    user_id: int,
    course_name: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    1. Save metadata to Postgres.
    2. Extract text, chunk it, embed it, push to Chroma.
    """
    try:
        await ingest_pdf(db, user_id, course_name, file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"status": "uploaded and ingested"}
