from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Hello World"}

@app.get("/greet")
def greet():
    return {"Message" : "Greetings"}

@app.get("/greet/{name}")
def greet_name(name: str):
    return {"Message" : f"Hello {name}"}