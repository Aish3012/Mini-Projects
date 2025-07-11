from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()
id=1
list=[]
catList=[]
x=[]

class inventory(BaseModel):
    name : str
    category : str
    cost : int
    qty : int
    id : Optional[int]=None
    
@app.get('/found')
def found():
    return{
        "isActive" : True
    }
    
@app.post('/createNewProduct')
def createNewProduct(invent : inventory):
    global id
    invent.id=id
    id=id+1
    list.append(invent)
    return{
        "isSuccess": True,
        "newProduct" : invent
    }

@app.get('/getList')
def getList():
    return{
        "list" : list
    }
    
    
@app.post('/Add/{count}')
def add(category : str, count : int, invent:inventory):
    for prod in list:
        if prod.category ==  category:
            catList.append(prod)

    for i in range(count):
        catList.append(invent)
        list.append(invent)
    print(catList)
    return{
        "is Success": True,
        "Updated category List": catList
    }

@app.delete('/delete/{count}')
def delete(category : str, count : int):
    print(count)
    for prod in list:
        if prod.category ==  category:
            x.append(prod)

    for i in range(count):
        print(x[i])
        a=x[i]
        x.remove(a)
        list.remove(a)
    return{
        "is success" : True,
        "updated list" : x
    }
    
