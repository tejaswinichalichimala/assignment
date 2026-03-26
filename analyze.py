from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional
from pipeline import process

router = APIRouter(tags=["Analyze"])

@router.post("/analyze")
async def analyze(
    file: Optional[UploadFile] = File(None),
    content: Optional[str] = Form(None)
):
    if file:
        text = (await file.read()).decode("utf-8")
    else:
        text = content

    return process({"content": text})