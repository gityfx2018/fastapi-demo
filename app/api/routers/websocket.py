from fastapi import APIRouter, Depends
from starlette.websockets import WebSocket, WebSocketDisconnect

from app.api.operation.users import get_user_info
from app.schemas.user import User

router = APIRouter()

#TODO Check if it works
@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket,
                             user: User = Depends(get_user_info)):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        await websocket.close()
