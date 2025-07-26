from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to my API!"}

# In order to start the live server, the command fastapi dev main.py doesn't works,
# we need to type python -m fastapi dev main.py

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title {payLoad['title']} content {payLoad['content']}"}

# continue to watch from 1:07:34