#for intialization
from fastapi import FastAPI
#for optional capabilites
from typing import Optional
from pydantic import BaseModel

#Fast API engine start
app = FastAPI()
#homepage stuff
@app.get("/")
def read_root():
    return {"Message": "Hello World"}
#greet page no parameters
@app.get("/greet")
def greet():
    return {"Message" : "Greetings"}
#using path parameter with a query parameter
@app.get("/greet/{name}")
def greet_name(name: str, age: Optional[int] = None):
    return {"Message" : f"Hello {name} and you are {age} old"}
#using only query parameter one required one optional
@app.get("/greets/")
def greet_name(name: str, age: Optional[int] = None):
    return {"Message" : f"Hello {name} and you are {age} old"}

class Student(BaseModel):
    name: str
    age: int
    roll: int

@app.post("/create_student")
def create_student(studnet_data: Student):
    return {
        "name": studnet_data.name,
        "age": studnet_data.age,
        "roll": studnet_data.roll
    }

