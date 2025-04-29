from fastapi import FastAPI
from app.routes import hello,openai
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000" ,
          "http://127.0.0.1:3000"   # For local React app
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests from listed origins
    allow_credentials=True,
    allow_methods=["*"],     # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],     # Allow all headers
)

app.include_router(hello.router)
app.include_router(openai.router)
