# @title
from fastapi import FastAPI

app = FastAPI(
    title="Bella Tavola API",
    description="API do restaurante Bella Tavola",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "restaurante": "Bella Tavola",
        "mensagem": "Bem-vindo à nossa API",
        "chef": "Livia Rainha",
        "cidade": "Rio de Janeiro",
        "especialidade": "Parmegianas"
    }

pratos = [
    {"id": 1, "nome": "Parmegiana de Frango", "categoria": "Parmegiana", "preco": 55.0},
    {"id": 2, "nome": "Parmegiana de Filé Mignon", "categoria": "Parmegiana", "preco": 70.0},
    {"id": 3, "nome": "Parmegiana de Berinjela", "categoria": "Parmegiana", "preco": 50.0},
    {"id": 4, "nome": "Tiramissu", "categoria": "Sobremesas", "preco": 25.0},
    {"id": 5, "nome": "Coca Cola", "categoria": "Bebidas", "preco": 8.0},
    {"id": 6, "nome": "Água", "categoria": "Bebidas", "preco": 5.0},
]

@app.get("/pratos")
async def listar_pratos():
    return pratos

@app.get("/pratos/{prato_id}")
async def buscar_prato(prato_id: int):
    for prato in pratos:
        if prato["id"] == prato_id:
            return prato
    return {"mensagem": "Prato não encontrado"}

from typing import Optional

@app.get("/pratos")
async def listar_pratos(
    categoria: Optional[str] = None,
    preco_maximo: Optional[float] = None
):
    resultado = pratos

    if categoria:
        resultado = [p for p in resultado if p["categoria"] == categoria]

    if preco_maximo:
        resultado = [p for p in resultado if p["preco"] <= preco_maximo]

    return resultado

@app.get("/pratos/{prato_id}/detalhes")
async def detalhes_prato(prato_id: int, incluir_ingredientes: bool = False):
    for prato in pratos:
        if prato["id"] == prato_id:
            if incluir_ingredientes:
                return {**prato, "ingredientes": ["...lista..."]}
            return prato
    return {"mensagem": "Prato não encontrado"}
