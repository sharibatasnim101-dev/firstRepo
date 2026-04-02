import logging
from fastapi import FastAPI, WebSocket, WebSocketDisconnect # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from typing import List

# Setting up the logger to show the function that called it (%(funcName)s)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s - [%(funcName)s]'
)

logger = logging.getLogger(__name__)

app = FastAPI()

# --- 1. Connection Manager (Handles connections/disconnections) ---
class ConnectionManager:
    def __init__(self):
        # List to hold all active websocket connections
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info(f"Client connected. Active connections: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        logger.info(f"Client disconnected. Active connections: {len(self.active_connections)}")

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

# --- 2. Adding CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://my-cool-app.example.com", # Fixed typo here
        "http://localhost:3000",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 3. Existing Route ---
@app.get("/")
def read_root():
    logger.info("Сервер ответил на запрос клиента")
    return {"message": "FastAPI is running in russian!"}

# --- 4. New WebSocket Route ---
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # 1. Accept the connection
    await manager.connect(websocket)
    
    try:
        # 2. Keep the connection alive and listen for data
        while True:
            data = await websocket.receive_text()
            logger.info(f"Received message: {data}")
            
            # 3. Send a response back (Echo)
            await manager.send_personal_message(f"Server reply: {data}", websocket)
            
    except WebSocketDisconnect:
        # 4. Handle Disconnect (This is where reconnection is handled on the server side)
        manager.disconnect(websocket)
        logger.info("Client disconnected cleanly.")