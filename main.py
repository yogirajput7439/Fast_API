from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI",
        "developer": "Python Developer"
    }

@app.get("/about")
def about():
    return {
        "name": "FastAPI",
        "framework": "Python"
    }