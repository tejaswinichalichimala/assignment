from fastapi import APIRouter
from search.elastic import search_logs

router = APIRouter(tags=["Search"])

@router.get("/search")
def search(q: str):
    return search_logs(q)