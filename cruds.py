from fastapi import FastAPI,Response
from ProductModel import Product,ProductData
from dbConnect import collection
from bson import ObjectId

app=FastAPI()

def root(response: Response):
    try:
        return{"isActive": True}
    except Exception as e:
        response.status_code=500
        return{
            "isSuccess":False,
            "msg":e
        }
        
async def create_Product(product: Product,response:Response):
    try:
        print(product)
        product_dict=dict(product)
        product_dict["isDelete"] = False  #by default flag isDelete=False
        result = await collection.insert_one(product_dict)
        response.status_code=201
        return{"message":"Product created successully","product":product,"result":str(result.inserted_id)}
    except Exception as e:
        response.status_code=500
        return{
            "isSuccess":False,
            "msg":e
        }
        
async def getProducts(response: Response):
    try:
        productsList=[]
        async for product in collection.find({"isDelete": False}): #find gives the list of all the items in database
            print(product)
            product["_id"]=str(product["_id"])   #convert object id to str
            productsList.append(product)
            
        return{"products" : productsList}
    except Exception as e:
        response.status_code=500
        return{
            "isSuccess":False,
            "msg":e
        }
        
async def getById(product_id: str,response:Response):
    try:
        product = await collection.find_one({"_id":ObjectId(product_id),"isDelete": False})
           
        if product :
            product["_id"]= str(product["_id"])
            return {"product": product}
        else:
            return{"error": "product not found"}
    except Exception as e:
        response.status_code=500
        return{
            "isSuccess":False,
            "msg":e
        }
        
async def deleteById(product_id:str,response:Response):
    try:
        print(product_id)
        await collection.delete_one({"_id":ObjectId(product_id),"isDelete": False})
        return{
            "isSuccess" : True,
            "product deleted":product_id
        }
    except Exception as e:
        response.status_code=500
        return{
            "isSuccess":False,
            "msg":e
        }
        
async def updateProduct(product_id:str,product:Product,response:Response):
    try:
        print(product)
        prod=await collection.find_one({"_id":ObjectId(product_id)})
        if prod:
            product_dict=dict(product)
            await collection.update_one({"_id":ObjectId(product_id),"isDelete": False},{"$set":product_dict})
            return{
                "isSuccess":True,
                "Updated product":product
                }
        else:
            return{
                "not found"
            }
    except Exception as e:
        response.status_code=500
        return{
            "isSuccess":False,
            "msg":e
        }
        
async def softDeleteById(product_id: str,response:Response):
    try:
        result = await collection.update_one(
            {"_id": ObjectId(product_id), "isDelete": False},
            {"$set": {"isDelete": True}}
        )
        if result.modified_count:
            return {"isSuccess": True, "msg": "Product soft deleted"}
        else:
            return {"isSuccess": False, "msg": "Product not found or already deleted"}
    except Exception as e:
        response.status_code=500
        return {
            "isSuccess": False,
            "msg": str(e)
            }