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
    Year : int


class updateStudent(BaseModel):
    Name : Optional[str] = None
    Age : Optional[int] = None
    Year : Optional[int] = None


@testApp.get("/")
def index():
    return {"Home" : "Sweet"}

@testApp.get("/get")
def get_student():
    return students

@testApp.get("/get/{student_id}")
def get_student(student_id: int = Path(gt=0)):
    if student_id not in students:
        return {"Error" : f"Student with id {student_id} not found!"}
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