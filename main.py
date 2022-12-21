from fastapi import FastAPI
from typing import List
import os
from model import Notes_create, Notes_info, Notes_list, Notes_text
import json
from datetime import datetime

app = FastAPI()

def pr_token():
    with open('token.txt', 'r') as file:
        id = file.read()
    return id



def filter():
    files = os.listdir(r'C:\Users\Lenova\PycharmProjects\Lab4')
    result = [0]
    ext = '.json'
    for filename in files:
        if filename.endswith(ext):
            filename = filename.replace('.json','')
            result.append(filename)
    return result

def create():
    files = filter()
    name = int(files[len(files)-1])+1
    with open(str(name)+'.json', 'w') as file:
        a = Notes_text(id=name, text='')
        b = Notes_info(creat=datetime.now(), updated=datetime.now())
        b = {k: str(v) for k, v in b.dict().items()}
        c = {
            'note' : a.dict(),
            'data' : b
        }
        json.dump(c, file)

    return name

@app.post('/create_note')
def create_note(token: str):
    if token == pr_token():
        id = Notes_create(id=create())
        return id
    else:
        return 'Неверный токен'

@app.get('/get_note')
def get_note(token: str, id:int):
    if token == pr_token():
        with open(str(id)+".json", "r") as file:
            notes = json.load(file)
        note = notes['note']
        a = Notes_text(id=note['id'], text=note['text'])
        return a
    else:
        return 'Неверный токен'

@app.patch('/up_note')
def up_note(token: str, id:int, text:str):
    if token == pr_token():
        with open(str(id)+".json", "r") as file:
            notes = json.load(file)
        notes['note']['text'] = text
        notes['data']['updated'] = str(datetime.now())
        with open(str(id)+".json", "w") as file:
            json.dump(notes, file)
        note = notes['note']
        a = Notes_text(id=note['id'], text=note['text'])
        return a
    else:
        return 'Неверный токен'

@app.get('/get_info')
def get_info(token: str, id:int):
    if token == pr_token():
        with open(str(id)+".json", "r") as file:
            notes = json.load(file)
        note = notes['data']
        c_d = datetime.strptime(note['creat'],"%Y-%m-%d %H:%M:%S.%f")
        u_d = datetime.strptime(note['updated'],"%Y-%m-%d %H:%M:%S.%f")
        a = Notes_info(creat=c_d, updated=u_d)
        return a
    else:
        return 'Неверный токен'

@app.delete('/delete_note')
def delete_note(token: str, id:int):
    if token == pr_token():
        path = r'C:\Users\Lenova\PycharmProjects\Lab4'+f'\{str(id)}.json'
        try:
            os.remove(path)
            return f'Заметка {id} удалена'
        except:
            return 'Заметки с таким id не найдено'
    else:
        return 'Неверный токен'

@app.get('/list_note')
def list_note(token: str):
    if token == pr_token():
        n_list : List[int] = list(map(int,filter()))
        n_list.remove(0)
        return Notes_list(notes_list=n_list)
    else:
        return 'Неверный токен'

print()