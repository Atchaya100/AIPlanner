from fastapi import APIRouter

router = APIRouter()

@router.get("/", methods=["GET", "HEAD"])
def greet():
    return {"message": "Hello from FastAPI on Mac!"}