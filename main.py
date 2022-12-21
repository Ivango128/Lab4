from fastapi import FastAPI, Query
import os
from model import Notes_create, Notes_info, Notes_list, Notes_text
import json

app = FastAPI()

def pr_token():
    with open('token.txt', 'r') as file:
        id = file.read()
    return id



def filter():
    files = os.listdir(r'C:\Users\Lenova\PycharmProjects\Lab4')
    result = []
    ext = '.json'
    for filename in files:
        if filename.endswith(ext):
            result.append(filename)
    return result

def create():
    files = filter()
    i = 0
    for file in files:
        i +=1
    name = i
    with open(str(name)+'.json', 'w') as file:
        note = {
            'id' : name,
            'text' : ''
        }
        a = Notes_text(**note)
        json.dump(a.dict(), file)

    return name

@app.post('/cr')
def creaate_note(token: str = Query(...,)):
    if token == pr_token():
        id = create()
        return id
    return 'Eror_create'