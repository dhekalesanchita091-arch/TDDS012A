from fastapi import FastAPI 
app=FastAPI()
@app.get('/')
def get():
    return {"message":"This is my FastAPI app"}
    @app.get("/view")
def view():
    students = [
        {
            "id": 1,
            "name": "Sanchita",
            "age": 19,
            "course": "BSc CS"
        },
        {
            "id": 2,
            "name": "Prachiti",
            "age": 20,
            "course": "BSc DS"
        }
    ]

    return students
