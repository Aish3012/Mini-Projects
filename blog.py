from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn  
app = FastAPI() #instance of FastApi
#fastapi compares each endpoint line by line, if matched it goes into the function

#"@app" is called path operation decorator and get is the operation of FastApi
@app.get('/blog')          
#the function is called path operation function
def blog(limit=100,published:bool=True,sort:Optional[str]=None):      
    if published:
        return { 'data': f'{limit} published blog from db' }
    else:
        return { 'data': f'{limit} blogs from db'}

@app.get('/blog/unpublished')
def unpublished():
    return { 'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):
    return{'data':id}


@app.get('/blog/{id}/comments')
def comments(id,limit:int=10):
    return limit
    #fetch comments of blog with id = id
    return { 'data':{'1','2'}}

class Blog(BaseModel):
    title:str
    body: str
    published : Optional[bool]

@app.post('/create')
def create(request:Blog):
    return {'data':f"Blog is created with title as {request.title}"}

#if __name__=="__learn_main__":
   # uvicorn.run(app,host="127.0.0.1",port='9000')