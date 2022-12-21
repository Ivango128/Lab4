from fastapi import FastAPI, Query
import os
from model import Notes_create, Notes_info, Notes_list, Notes_text

app = FastAPI()


def filter():
    files = os.listdir('C:\Users\lenovo\PycharmProjects\Lab4')
    result = []
    ext = '.json'
    for filename in files:
        if filename.endswith(ext):
            result.append(filename)
    return result

def create():
    files = os.listdir('C:\Users\lenovo\PycharmProjects\Lab4')
    i = 0
    for file in files:
        name = os.path.splitext()[0]
        i +=1
    name = i+1

@app.post('/cr')
def creaate_note(id:Notes_create, token: str = Query(...,)):
    return id