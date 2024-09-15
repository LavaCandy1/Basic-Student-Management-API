# FastAPI Student Management API

This is a basic RESTful API built using FastAPI that simulates managing a collection of students. It provides endpoints to get, add, update, and delete student records.

## Prerequisites

- Python 3.8 or later
- FastAPI
- Uvicorn (for running the server)
- Pydantic (for data validation)

## Installation

1. Clone the repository or copy the project files.
2. Install the required dependencies:
   pip install -r requirements.txt

3. Run the FastAPI app using Uvicorn:
   uvicorn <filename>:testApp --reload
   Replace <filename> with the name of the Python file containing the FastAPI code.

4. Navigate to http://127.0.0.1:8000 to access the API.

## Endpoints

1. "/" -> basic home endpoint

- GET Methods

2. "/get" -> get details of all students
3. "/get/{student_id}" -> get details of a perticular student
4. "/get-by-name" -> get details of student using name

- POST Methods

5. "/create-student/{student_id}" -> create a new student using student id

- PUT Methods (update)

6. "/update-student/{student_id}" -> update details of a student using student id
   Request body with optional fields for updating
   {
   "Name": "John",
   "Age": 22,
   "Year": "4"
   }

- DELETE Methods

7. "/delete" -> delete student details using student id
   student_id in request body

## Data Model

- Student

  {
  "Name": "string",
  "Age": "integer",
  "Year": "integer"
  }

- UpdateStudent

  {
  "Name": "string (optional , default = None)",
  "Age": "integer (optional , default = None)",
  "Year": "integer (optional , default = None)"
  }

## Running API

You can test the API using any API client like Postman or cURL, or directly through **the built-in FastAPI documentation** available at http://127.0.0.1:8000/docs.

This `README.md` file includes details about how to set up and run your FastAPI project, the available API endpoints, and the data models used.
