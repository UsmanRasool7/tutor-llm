
from fastapi import FastAPI
from dotenv import load_dotenv


from app.db.session import engine
from app.db.base    import Base
from app.db.models import CourseMaterial
print("After importing CourseMaterial, tables:", list(Base.metadata.tables.keys()))



print("SQLAlchemy tables before create_all:", list(Base.metadata.tables.keys()))

load_dotenv()

app = FastAPI(
    title="LLM Tutor",
    description="Swagger interface to test endpoints for LLM Tutor",
    version="1.0.0",
)


Base.metadata.create_all(bind=engine)


print("SQLAlchemy tables after create_all:", list(Base.metadata.tables.keys()))


from app.routers.example   import router as example_router
from app.routers.llm       import router as llm_router
from app.routers.materials import router as materials_router
from app.routers.tutor     import router as tutor_router

app.include_router(example_router)
app.include_router(llm_router)
app.include_router(materials_router)
app.include_router(tutor_router)

@app.get("/health")
def health():
    return {"status": "ok"}
