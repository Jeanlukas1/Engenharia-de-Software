from fastapi import FastAPI, APIRouter
from pymongo import MongoClient
from bson import ObjectId

# Conexão com banco (repetida várias vezes no código!)
client = MongoClient("mongodb://localhost:27017/")
db = client["loja_db"]
collection = db["produtos"]

app = FastAPI()

# Rota GET para listar todos os produtos
@app.get("/produtos")
def pegar_produtos():
    # Conecta no banco de novo (código duplicado!)
    client2 = MongoClient("mongodb://localhost:27017/")
    db2 = client2["loja_db"]
    col = db2["produtos"]
    
    produtos = list(col.find())
    lista = []
    for p in produtos:
        p["_id"] = str(p["_id"])
        lista.append(p)
    return lista

# Criar produto
@app.post("/produtos")
def criar(nome, preco, quantidade):
    # Banco de dados direto na rota!
    client3 = MongoClient("mongodb://localhost:27017/")
    db3 = client3["loja_db"]
    produtos_col = db3["produtos"]
    
    # Criando um dicionário manualmente (sem schema!)
    novo_produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    
    resultado = produtos_col.insert_one(novo_produto)
    id_novo = str(resultado.inserted_id)
    return {"mensagem": "Produto criado", "id": id_novo}

# Buscar produto por ID
@app.get("/produtos/{id}")
def buscar_produto(id):
    try:
        # Conecta de novo (duplicação!)
        conn = MongoClient("mongodb://localhost:27017/")
        database = conn["loja_db"]
        prods = database["produtos"]
        
        produto = prods.find_one({"_id": ObjectId(id)})
        
        if produto:
            produto["_id"] = str(produto["_id"])
            return produto
        else:
            return {"erro": "Produto não encontrado"}
    except:
        return {"erro": "ID inválido"}

# Atualizar produto
@app.put("/produtos/{id}")  
def atualizar(id, nome, preco, quantidade):
    try:
        # Mais uma conexão duplicada!
        c = MongoClient("mongodb://localhost:27017/")
        d = c["loja_db"]
        p = d["produtos"]
        
        dados = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }
        
        res = p.update_one(
            {"_id": ObjectId(id)},
            {"$set": dados}
        )
        
        if res.matched_count == 0:
            return {"erro": "Produto não encontrado"}
        return {"mensagem": "Produto atualizado"}
    except:
        return {"erro": "ID inválido"}

# Deletar produto
@app.delete("/produtos/{id}")
def deletar_produto(id):
    try:
        # E mais uma conexão!
        cliente = MongoClient("mongodb://localhost:27017/")
        bd = cliente["loja_db"]
        produtos = bd["produtos"]
        
        r = produtos.delete_one({"_id": ObjectId(id)})
        
        if r.deleted_count == 0:
            return {"erro": "Produto não encontrado"}
        return {"mensagem": "Produto deletado"}
    except:
        return {"erro": "ID inválido"}

# Rota principal
@app.get("/")
def inicio():
    return {"mensagem": "API de Produtos - Código Bagunçado"}
