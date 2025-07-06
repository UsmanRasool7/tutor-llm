import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.chroma_client import client
from app.db.models import CourseMaterial
from app.db import models
from fastapi import UploadFile, HTTPException


embed_model = SentenceTransformer(settings.EMBEDDING_MODEL)

async def ingest_pdf(
    db: Session,
    user_id: int,
    course_name: str,
    file: UploadFile
):
    
    course = models.CourseMaterial(
        user_id=user_id,
        name=course_name
    )
    db.add(course)
    db.commit()
    db.refresh(course)

    
    contents = await file.read()
    doc = fitz.open(stream=contents, filetype="pdf")
    text = "".join(page.get_text() for page in doc)

   
    chunks = [
        text[i : i + settings.CHUNK_SIZE]
        for i in range(0, len(text), settings.CHUNK_SIZE)
    ]

  
    col_name = f"user_{user_id}_course_{course.id}"
    collection = client.get_or_create_collection(col_name)


    for idx, chunk in enumerate(chunks):
        emb = embed_model.encode(chunk).tolist()
        collection.add(
            documents=[chunk],
            embeddings=[emb],
            ids=[f"{course.id}_{idx}"],
        )
