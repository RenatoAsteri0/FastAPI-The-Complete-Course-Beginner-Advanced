from fastapi import FastAPI, Body

app = FastAPI()


class Book:
    id: int
    titulo: str
    autor: str
    descricao: str
    avaliacao: int

    def __init__(self, id, titulo, autor, descricao, avaliacao):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.descricao = descricao
        self.avaliacao = avaliacao

BOOKS = {
    Book(1, 'titulo um', 'renato', 'um livro bem legal', 8),
    Book(2, 'titulo dois', 'leticia', 'um livro muito legal', 9),
    Book(3, 'titulo tres', 'renato', 'um livro excelente', 10),
    Book(4, 'titulo quatro', 'joao', 'um livro ruim', 3)
}

@app.get("/books")
async def listar_livros():
    return BOOKS