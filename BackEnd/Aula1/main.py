from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    mensagem = saudacao("Jean")
    
    somadenum = soma(10, 10)
    
    return templates.TemplateResponse(
        "index.html",
        {"request": request,
         "mensagem": mensagem, 
         "somadenum": somadenum,
         }
    )
    
def saudacao(nome: str):
    return f"Olá, {nome}! 👋"

def soma(num1: int, num2: int):
    soma = num1 + num2
    
    return f"a soma do {num1} + {num2} = {soma}"
