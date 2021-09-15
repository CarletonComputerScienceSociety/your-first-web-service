from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

## app setup
app = FastAPI()
templates = Jinja2Templates(directory="templates")


## data
items = ["apple", "banana", "orange"]


## base route
@app.get("/")
def read_root():
    return {"Hello": "World"}


## page routes
@app.get("/items/{id}", response_class=HTMLResponse)
def read_item(request: Request, id):
    return templates.TemplateResponse(
        "item.html", 
        {
            "request": request, 
            "item": items[int(id)]
        }
    )

@app.get("/create")
def create_form(request: Request):
    message = "What is the name of your new item?"
    return templates.TemplateResponse(
        "create.html", 
        {
            "request": request, 
            "message": message
        }
    )

@app.post("/create")
def create_item(request: Request, item = Form(...)):
    # add new item to items list
    items.append(item)
    message = "Succesfully Added Item."

    # return updated list
    return templates.TemplateResponse(
        "create.html", 
        {
            "request": request, 
            "message": message
        }
    )


## API routes
@app.get("/api/items")
def read_items():
    return {"items": items}

@app.get("/api/items/{item_id}")
def read_item(item_id):
    return {"item": items[int(item_id)]}