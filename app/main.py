from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from app.api import endpoints

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(endpoints.router)

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})