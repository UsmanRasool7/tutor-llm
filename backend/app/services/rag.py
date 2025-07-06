from sentence_transformers import SentenceTransformer
from app.core.config import settings
from app.core.chroma_client import client

embed_model = SentenceTransformer(settings.EMBEDDING_MODEL)

PROMPT_TEMPLATE = """
You are a helpful, patient tutor. Use ONLY the Course Material below to answer the student’s question.
If the answer is not in the material, say “I’m not sure—please check your materials.”

Course Material:
{context}

Question:
{question}

Answer:
"""

def retrieve_context(user_id: int, course_id: int, question: str) -> str:
    col_name = f"user_{user_id}_course_{course_id}"
    collection = client.get_collection(col_name)
    q_emb = embed_model.encode(question).tolist()
    result = collection.query(
        query_embeddings=[q_emb],
        n_results=settings.TOP_K
    )
    chunks = result["documents"][0]
    return "\n\n---\n\n".join(chunks)
