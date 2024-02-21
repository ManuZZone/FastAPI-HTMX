from typing import Union
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

views = Jinja2Templates(directory="views")


@app.get("/")
def _(request: Request):
    return views.TemplateResponse(request=request, name="index.html")

counter: int = 0

@app.get("/test")
def _(request: Request):
    global counter
    counter+=1
    print(request.session['counter'])
    return views.TemplateResponse(request=request, name="partials/after_button_ciao.html", context={"text": counter}, headers={"HX-Retarget": "this", "HX-Reswap": "outerHTML"})

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}