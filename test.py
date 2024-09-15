from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

testApp = FastAPI()


students = {
    1 : {
        "Name":"Ayush",
        "Age":20,
        "Year":3
    },
    2 : {
        "Name":"Harsh",
        "Age":20,
        "Year":3
    }
}


class Student(BaseModel):
    Name : str
    Age : int
    Year : str


class updateStudent(BaseModel):
    Name : Optional[str] = None
    Age : Optional[str] = None
    Year : Optional[str] = None


@testApp.get("/")
def index():
    return {"First" : "Name"}

@testApp.get("/get/{student_id}")
def get_student(student_id: int ):
    return students[student_id]

@testApp.get("/get-by-name")
def get_student(student_name: str , test:int):
    for student in students:
        if student_name == students[student]["Name"]:
            return students[student]
        
    return {"Error":"Name dosen't exist"}

@testApp.post("/save-student/{student_id}")
def save_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error" : "Id exists!"}
    
    students[student_id] = student
    print(students)
    return students[student_id]

@testApp.put("/update-student/{student_id}")
def update_student(student_id : int , student : updateStudent):
    if student_id not in students:
        return {"Error" : "Student ID not found"}
    
    if student.Name is not None:
        students[student_id]["Name"] = student.Name
    if student.Age is not None:
        students[student_id]["Age"] = student.Age
    if student.Year is not None:
        students[student_id]["Year"] = student.Year

    return students[student_id]


@testApp.delete("/delete")
def delete_student(student_id : int):
    if student_id not in students:
        return {"Error" : "Student ID not found"}
    
    del students[student_id]
    return {"Message" : f"Student with id {student_id} was deleted"}