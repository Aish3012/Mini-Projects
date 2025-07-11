from fastapi import FastAPI

#creaate a fastapi application
app=FastAPI()

#define a route at the root/endpoint web address("/")
#@app.get("/")
@app.get("/qqqa")
def read_root():
    return {
        "message: Hello FastApi!"
    }
    
    from fastapi import FastAPI



#http://127.0.0.1:8000  (web ip address)        http-protocol, 127.0.0.1-ip address, 8000-port number
#uvicorn main:app --reload  (to execute)
#pip insstall uvicorn rn fastapi pydantic motor