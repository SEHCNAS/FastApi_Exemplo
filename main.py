from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

#Inicializa o fastApi
app = FastAPI()

#Cria um base de dados temporaria
Vendas = [
    {"Id":1,"Item":"Garrafa 1L", "Preco": 7.25, "Quantidade":5},
    {"Id":2,"Item":"Lata", "Preco": 3.50, "Quantidade":10},
    {"Id":3,"Item":"Garrafa 750", "Preco": 5.00, "Quantidade":3},
    {"Id":4,"Item":"Bolacha", "Preco": 1.99, "Quantidade":1}
]

#Cria um modelo de dados
class Item(BaseModel):
    Id: int
    Item: str
    Preco: float
    Quantidade: int


#api caso chame o root
@app.get("/")
async def root():
    return {"message": "Hello World"}


#Api que retorna uma mensagem
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


#Retorna todas as vendas
@app.get("/Venda")
def Busca_Todas_As_Vendas():
    return Vendas


#Retorna uma venda especifica
@app.get("/Venda/{Id}")
def Busca_Todas_As_Vendas(Id:int, needy: str):
    return Vendas.__getitem__(Id)


#Adiciona um item a venda, usando como modelo a classe Item
@app.post("/Venda")
def Adicionar_Venda(item: Item):
    Item_Encoded = jsonable_encoder(item)
    Vendas.append(Item_Encoded)
    return Vendas


