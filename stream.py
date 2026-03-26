from fastapi import APIRouter, WebSocket

router = APIRouter(tags=["Stream"])

clients = []

@router.websocket("/ws")
async def ws(ws: WebSocket):
    await ws.accept()
    clients.append(ws)

    while True:
        msg = await ws.receive_text()
        for c in clients:
            await c.send_text(msg)