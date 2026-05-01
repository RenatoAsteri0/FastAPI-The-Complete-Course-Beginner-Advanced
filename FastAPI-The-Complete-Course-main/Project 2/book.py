from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

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


class Book_Request(BaseModel):
    id: Optional[int] = Field("Campo não é necessário", default=None)
    titulo: str = Field(min_length=3, max_length=20)
    autor: str
    descricao: str
    avaliacao: int = Field(ge=0, le=10)


BOOKS = [
    Book(1, 'titulo um', 'renato', 'um livro bem legal', 8),
    Book(2, 'titulo dois', 'leticia', 'um livro muito legal', 9),
    Book(3, 'titulo tres', 'renato', 'um livro excelente', 10),
    Book(4, 'titulo quatro', 'joao', 'um livro ruim', 3)
]

@app.get("/books")
async def listar_livros():
    return BOOKS

@app.post("/create-book")
async def criar_livro(book_request: Book_Request):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)
    return new_book

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book