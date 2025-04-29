from fastapi import FastAPI
from app.routes import hello, openai
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"  # For local React app
]

# ✅ Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include routers
app.include_router(hello.router)
app.include_router(openai.router)

# ✅ Finally, run only if local
if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.environ.get('PORT', 8000))  # Default 9000 locally
    uvicorn.run("main:app", host="0.0.0.0", port=port)
