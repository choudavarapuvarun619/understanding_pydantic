from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class student(BaseModel):
    name:str
    age:int

@app.post("/students")
def add_student(student:student):
    return {
        "message":"student verified and added successfully",
        "student":student
    }
