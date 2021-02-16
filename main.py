from fastapi import FastAPI
from parsers import parsing


app = FastAPI()


@app.get("/{query}")
def index(query: str):
    response = parsing(query)
    return {'Запрос': query, 'Ссылка на картинку': response[0], 'Цена': response[1]}


@app.get("/{item}/{discription}")
def read_item(item: str, discription: str):
    response = parsing(discription)
    return {'Описание': discription, 'Ссылка на картинку': response[0], 'Цена': response[1]}

