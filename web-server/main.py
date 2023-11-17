#https://fastapi.tiangolo.com/ to review 

import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get("/contact", response_class=HTMLResponse)
def get_list():
    return """
    <H1>Hola Soy una página</H1>
    <p>Soy un Parrafo</p>
    """ 


def run():
    store.get_categories()
    
    
if __name__ == '__main__':
    run()