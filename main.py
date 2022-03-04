from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello dog!"}

@app.get("/posts")
def get_posts():
    return [
        {"id": 1, "title": "Hello earth"},
        {"id": 2, "title": "Hello Mars"},
        {"id": 3, "title": "Hello Jupiter"}
    ]