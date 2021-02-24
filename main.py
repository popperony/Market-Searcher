from fastapi import FastAPI

from parsers import parsing
from models import Queries


# uvicorn main:app --reload
app = FastAPI()


@app.get("/{query}")
def index(query: str):
    response = parsing(query)
    try:
        return {'Request': query, 'link_image_1': response[0][0], 'link_image_2': response[0][1], 'link_image_3': response[0][2], 'average_price': response[1]}
    except IndexError:
        return {'Request': query,'Error': 'no result or parser was blocked'}


@app.get("/{query}/{discription}")
def read_item(query: str, discription: str):
    response = parsing(discription)
    try:
        return {'Request': discription, 'link_image_1': response[0][0], 'link_image_2': response[0][1], 'link_image_3': response[0][2], 'average_price': response[1]}
    except IndexError:
        return {'Request': discription,'Error': 'no result or parser was blocked'}

@app.post("/query")
def add_queries(item: Queries):
    print(item.get('query'))
    return item