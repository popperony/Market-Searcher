from fastapi import FastAPI
from parsers import parsing


# uvicorn main:app --reload
app = FastAPI()


@app.get("/{query}")
def index(query: str):
    response = parsing(query)
    return {'Request': query, 'link_image_1': response[0][0], 'link_image_2': response[0][1], 'link_image_3': response[0][2], 'average_price': response[1]}


@app.get("/{item}/{discription}")
def read_item(item: str, discription: str):
    response = parsing(discription)
    return {'Описание': discription, 'Ссылка на картинку': response[0], 'Цена': response[1]}
