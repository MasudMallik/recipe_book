from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,RedirectResponse
from pydantic import BaseModel
from typing import List,Optional

app=FastAPI()
app.mount("/static",StaticFiles(directory="recipe_book/static"),name="static")
templates=Jinja2Templates(directory="recipe_book/templates")

@app.get("/",response_class=HTMLResponse)
def home(request):
    return templates.TemplateResponse("login.html",{"request": request})