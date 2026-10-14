from fastapi import FastAPI
import requests
app=FastAPI()

#GET ALL EXTERNAL DATA
@app.get("/posts")
def get_posts():
    url="https://jsonplaceholder.typicode.com/posts"
    response=requests.get(url)
    return response.json()

#GET DATA BASED ON ID
@app.get("/posts/{post_id}")
def get_posts(post_id:int):
    url=f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response=requests.get(url)
    return response.json()
