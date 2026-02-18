from fastapi import FastAPI, HTTPException
from database import students, professors
from typing import Optional, List
from models import Student, professor, Feedback
from nlp_utils import analyze_sentiment, smart_search
# from unit_testing.test_main import client

app = FastAPI(
    title = "AI Powered Student Management API",
    description = "A simple REST API using FastAPI (CRUD)",
    version = "1.0.0"
)

@app.get('/')
def home():
    return {"message": "Welcome to Student Management API...🚀"}

@app.get('/about')
def about():
    return {"info": "This is my first API"}


# STUDENT CONTROLLERS

@app.get('/student/all', response_model = List[Student])
def get_all_student():
    return students

@app.get('/student/{id}', response_model = Student)
def get_student(id:int):
    if id < 0 or id >= len(students):
        raise HTTPException(
            status_code = 404,
            detail = "Student not found"
        )
    return students[id]

@app.post('/student', response_model = Student)
def create_student(student: Student):
    students.append(student)
    return students[-1]

@app.put('/student/{id}')
def update_student(id: int, updated_student: Student):
    if id < 0 or id >= len(students):
        raise HTTPException(
            status_code = 404,
            detail = "Student not found"
        )
    students[id] = updated_student
    return {
        "message": "Student updated successfully",
        "data": updated_student
    }

@app.delete('/student/{id}')
def delete_student(id: int):
    if id < 0 or id >= len(students):
        raise HTTPException(
            status_code = 404,
            detail = "Student not found"
        )
    students.pop(id)
    return {
        "message": "Student deleted successfully"
    }

@app.get("/filter")
def search_student(query:str):
    # result = [s for s in students if name.lower() in s.name.lower()]
    result = smart_search(students, query)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="No student found with this name"
        )
    
    return{
        "count":len(result),
        "search_result":result
    }


# PROFESSOR CONTROLLERS

@app.get('/professor/{id}', response_model = professor)
def get_professor(id:int):
    if id < 0 or id >= len(professors):
        raise HTTPException(
            status_code = 404,
            detail = "Professor not found"
        )
    return professors[id]

@app.get('/professor/all', response_model = List[professor])
def get_all_professor():
    return professors

@app.post('/professor')
def create_professor(professor: professor):
    professors.append(professor)
    return professors[-1]


# FEEDBACK
@app.post('/analyse-sentiment')
def sentiment_analysis(feedback: Feedback):
    sent_analysis = analyze_sentiment(feedback.text)
    return {
        "text": feedback.text,
        "analysis":{
            "polarity": sent_analysis[1],
            "sentiment": sent_analysis[0]
        }
    }

