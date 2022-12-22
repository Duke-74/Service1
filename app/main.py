from fastapi import FastAPI, HTTPException

from app.name import Name

app = FastAPI()

names : list[Name] = [
    Name(0, 'Ivan'),
    Name(1, 'Maria'),
    Name(2, 'Irina'),
    Name(3, 'Anton'),
    Name(4, 'Natalia'),
    Name(5, 'Alexandr'),
    Name(6, 'Maxim'),
    Name(7, 'Daniil'),
    Name(8, 'Alexandra'),
    Name(9, 'Victoria'),
    Name(10, 'Mickhail')
]

@app.get("/v1/allnames")
async def get_all_names():
    return names

@app.get("/v1/allnames/{id}")
async def get_name_by_id(id: int):
    result = [item for item in names if item.id == id]
    if len(result) > 0:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail="Name not found")

@app.get("/v1/__health")
async def get_health():
    return "200"
