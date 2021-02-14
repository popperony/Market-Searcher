from fastapi import FastAPI
from parsers import ozon_parsing, google_engine


app = FastAPI()


@app.get("/{query}")
def index(query: str):
    value = query
    return {'Google': value}


@app.get("/ins/{item}/{discription}")
def read_item(item: str, discription: str):
    return {"item" : item, "discription": discription}


