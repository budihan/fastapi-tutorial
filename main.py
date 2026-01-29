from fastapi import FastAPI

app = FastAPI()

@app.get('/') #decorate with base url
def index():
    return {'data': {'name': 'Budi'}}

@app.get('/about')
def about():
    return {'data': 'about page'}