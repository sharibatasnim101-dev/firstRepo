import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Setting up the logger to show the function that called it (%(funcName)s)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s - [%(funcName)s]'
)

logger = logging.getLogger(__name__)

app = FastAPI()

# Adding CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://my-cool-app.example.com",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    logger.info("Server replied to client's request")
    return {"message": "FastAPI is running"}