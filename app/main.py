from fastapi import FastAPI, Request
import pathlib
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

BASE_DIR = pathlib.Path(__file__).parent
# print((BASE_DIR / "template").exists())

app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "template"))
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "abc": 123})

@app.post("/")
def home_detail():
    return{"hello": "world"}