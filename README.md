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

### get

2. "/get" -> get details of all students
3. "/get/{student_id}" -> get details of a perticular student
