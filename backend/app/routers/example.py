from app.services.example import example_function
from fastapi import APIRouter


router = APIRouter(prefix="/example_endpoints", tags=["Example"])

@router.get("/example")
def example_endpoint():
    """
    Example endpoint that returns a message.
    This endpoint is used to demonstrate how to create an endpoint in FastAPI.
    """
    return example_function()