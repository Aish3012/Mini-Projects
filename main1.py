import asyncio   #asynchronous library
from first import add,mycred

result=add(5,10)
print(result)
print(mycred)

async def add(a,b):       #async keyword is for making the function asynchronous
    await asyncio.sleep(10)   #await keyword is used for sleep and sleep is the function of asyncio library 
    return a+b
    
res=asyncio.run(add(4,5))     #run is the function of asyncio library 
print(res)

async def main():
    #result=await add(5,10)
    result=await asyncio.gather(      #gather is the function of asyncio library to complete all the tasks in parallel
        add(5,5),
        add(6,7),
        add(8,10)
        )
    print(result)
    
async def func1():
    print("one")
    await asyncio.sleep(5)
    await func2()     #await func2() will make func() wait untill the func2() complets
    print("four")
    await asyncio.sleep(5)
    print("five")
    await asyncio.sleep(5)
    
async def func2():
    await asyncio.sleep(5)
    print("two")
    await asyncio.sleep(5)
    print("three")

async def func3():
    task=asyncio.create_task(func4())     #create_task makes the other function passed run anytime if there is any free time
    print("one")
    print("four")
    await asyncio.sleep(2)
    print("five")
    await asyncio.sleep(2)

async def func4():
    print("two")
    await asyncio.sleep(2)
    print("three")


    
    
asyncio.run(main())
asyncio.run(func1())
asyncio.run(func3())
#mongodb+srv://aish:aish3012@cluster0.soi2vbt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
