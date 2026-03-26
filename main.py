from fastapi import FastAPI

from routes.analyze import router as analyze_router
from routes.stream import router as stream_router
from routes.search import router as search_router

app = FastAPI()

app.include_router(analyze_router)
app.include_router(stream_router)
app.include_router(search_router)

@app.get("/")
def home():
    return {"status": "running"}