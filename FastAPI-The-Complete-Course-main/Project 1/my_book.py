from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/books")
async def first_api():
    return BOOKS

@app.get("/books/{buscar_ator}")
async def buscar_todos_por_ator(ator: str):
    book_return = []
    for i in range(len(BOOKS)):
        if BOOKS[i].get('author').casefold() == ator.casefold():
            book_return.append(BOOKS[i])
    return book_return


@app.get("/books/{dynamic_title}")
async def read_a_book(dynamic_title: str):
    for book in BOOKS:
        if book['title'].casefold() == dynamic_title.casefold():
            return book

@app.post("/book/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)