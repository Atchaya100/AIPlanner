from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def greet():
    return {"message": "Hello from FastAPI on Mac!"}


@router.head("/")
def head_greet():
    return {"message": "Hello from FastAPI on Mac!"}