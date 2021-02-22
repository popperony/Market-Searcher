from fastapi import FastAPI
from parsers import parsing


# uvicorn main:app --reload
app = FastAPI()


@app.get("/{query}")
def index(query: str):
    response = parsing(query)
    return {'Запрос': query, 'Ссылка на картинку 1': response[0][0], 'Ссылка на картинку 2': response[0][1], 'Ссылка на картинку 3': response[0][2], 'Средняя цена': response[1]}


@app.get("/{item}/{discription}")
def read_item(item: str, discription: str):
    response = parsing(discription)
    return {'Описание': discription, 'Ссылка на картинку': response[0], 'Цена': response[1]}
