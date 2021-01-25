from fastapi import FastAPI
from google_search_engine import GESearch

app = FastAPI()


@app.get("/{query}")
def index(query: str):
    return {'Key': GESearch(query)}


@app.get("/ins/{item}/{discription}")
def read_item(item: str, discription: str):
    return {"item" : item, "discription": discription}


