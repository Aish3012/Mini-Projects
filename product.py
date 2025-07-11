from fastapi import FastAPI,Response
from pydantic import BaseModel
from typing import Optional

app=FastAPI()
productsList=[]
id=1


@app.get('/heartbeat')
def myfunc(response : Response):
    try:
        return {
        "isActive" : True
    }
    except Exception as e:
        response.status_code = 500
        return{
            "is Success" : False,
            "msg" : e
        }

    

    
class product(BaseModel):
    name : str
    cost : int
    category : str
    qty : int
    id : Optional[int]=None


    
@app.post('/createProduct')
def createProduct(prod : product,response : Response):
    try:
        #print(prod)
        global id
        prod.id=id
        id=id+1
        productsList.append(prod)
        response.status_code = 201
        return{
            "isSucces" : True,
            "product " : prod
        }
    except Exception as e:
        response.status_code = 500
        return{
            "is Success" : False,
            "msg" : e
        }
    

  

@app.get('/getProducts')
def getProduct(response : Response):
    try:
        print(productsList)
        return{
            "isSuccess" : True,
            "productsList" : productsList
        }
    except Exception as e:
        response.status_code = 500
        return{
            "is Success" : False,
            "msg" : e
        }
    

    
@app.get('/getProduct/{prodId}')
def getProducts(prodId : int,response : Response):
    try:
        print(prodId)
        x= None
        for prod in productsList:
            if prod.id == prodId:
                x = prod
            
        if x == None:
            x = "prod not found"
    
        return{
            "isSuccess" : True,
            "productsList" : x
        }
    except Exception as e:
        response.status_code = 500
        return{
            "is Success" : False,
            "msg" : e
        }

    

  
@app.delete("/deleteProduct/{prodId}")
def deleteProduct(prodId : int,response : Response):
    try:
        x=None
        print(prodId)
        for prod in productsList:
            if prod.id == prodId:
                x=prod
        if x==None:
            return{
                "isDelete" : False,
                "message" : "product not found"
            }
        else:
            productsList.remove(x)
            return{
                    "isDelete" : True,
                    "message" : f"product with id {prodId} is delete"
                    }
    except Exception as e:
        response.status_code = 500
        return{
            "is Success" : False,
            "msg" : e
        }
    

@app.put("/updateProduct/{prodId}")
def updateProduct(prodId : int, prod : product,response : Response):
    try:
        x= None
        for i in range(0,len(productsList),1):
            if productsList[i].id == prodId:
                x = i
            
        if x == None:
            x = "product not found"
        else:
            productsList[x]=prod
            x=prod 
    
        return{
            "isSuccess" : True,
            "UpdatedProduct" : x
        }
    except Exception as e:
        response.status_code = 500
        return{
            "is Success" : False,
            "msg" : e
        }
        
@app.put('/updateProductByEnum/{prodId}')
def updateProductByEnumeration(prodId : int,prod: product):
    idx = 0
    for index,product in enumerate(productsList):
        if product.id == prodId:
            idx = index
    
    productsList[idx] = prod
       
    return {
            "isSuccess" :True,
            "Updated Product" : prod
        }
        
@app.get('/getprodByCat')
def getByQuery(category : Optional[str]=''):
    print("in api")
    print(category)
    x=[]
    for prod in productsList:
        if prod.category == category:
            x.append(prod)
    return{
        "data" :x
    }
   
    
    
    
   
                
  
            
            


    