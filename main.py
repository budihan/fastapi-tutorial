from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Blog(BaseModel):
    title: str 
    body: str
    published: Optional[bool]

# FastAPI decorators to define paths, GET operator and path operation function
@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # only return 10 published blogs
    if published:
        return {'data': f'published {limit} blogs'}
    else:
        return {'data': f'unpublished {limit} blogs'}
    
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished blogs'}

# path with dynamic routing
@app.get('/blog/{id}')
def show(id: int):
    # show blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id, limit = 10):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}

@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'blog created with {request.title}'}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)