from fastapi import FastAPI

app = FastAPI()







@app.get("/")

def home():
    return {
        "message" : "Welcome to my First FASTAPI assignment"
    }

@app.get("/about")
def about():
    return {
        "student_name" : "Vardaan","course" : "FastAPI", "status" : "Learning","topic":"First API Assignment"
    }

@app.get("/trainer")
def trainer():
    return {
        "name":"Hemanth", "role":"Trainer", "subject":"FastAPI"
    }

@app.get("/courses")
def courses():
    return [
        {
            "id": "1",
            "name": "Python Bascis",
            "duration": "1 week"
        },
        {
            "id":"2",
            "name":"FastAPI",
            "duration":"2 week"
        },
        {
            "id":"3",
            "name":"SQL Bascis",
            "duration":"1 week"
        }
    ]

@app.get("/students")
def students():
    return [
        {
            "id":1, "name":"Akhil", "course":"Python", "city":"Hyderabad"
        },
        {
            "id":2, "name":"Sai", "course":"Python", "city":"Vijaywada"
        },
        {
            "id":3, "name":"Vardaan", "course":"Python", "city":"Jammu"
        }
    ]

@app.get("/college")
def college():
    return{
        "college_name": "MIET",
        "location"  : "Kotbhalwal",
        "department": "CSE(CS)",
        "current_module": "FastAPI"
    }

@app.get("/technologies")
def technologies():
    return {
        "Python","FastAPI","JSON","HTTP","REST API"
    }
