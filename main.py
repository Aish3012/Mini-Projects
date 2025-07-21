from fastapi import FastAPI,Response
from ProductModel import Product,ProductData
from bson import ObjectId
from cruds import root,create_Product,getProducts,getById,deleteById,updateProduct,softDeleteById


app=FastAPI()

@app.get('/heartbeat')
async def fun1(response: Response):
    return await root({response: Response})


@app.post('/products')
async def fun2(product: Product,response:Response):
    return await create_Product(product,response)
        
@app.get('/getProducts')
async def func3(response: Response):
    return await getProducts(response)
    

@app.get('/getById/{product_id}')
async def func4(product_id: str,response:Response):
    return await getById(product_id,response)

        
@app.delete('/deleteById/{product_id}')
async def func5(product_id:str,response:Response):
    return await deleteById(product_id,response)
        
    
@app.put('/updateProduct/{product_id}')
async def func6(product_id:str,product:Product,response:Response):
    return await updateProduct(product_id,product,response)
        
@app.put('/softDeleteById/{product_id}')
async def func7(product_id: str,response:Response):
    return await softDeleteById(product_id,response)


    
    
    

        

       
        
        
        
        