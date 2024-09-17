from fastapi import APIRouter, Body, HTTPException
from models.book_schema import Book_model as BookSchema
from database import Book_model, Author

book_route = APIRouter()

@book_route.post("/", response_model=BookSchema)
def create_book(book: BookSchema = Body(...)):

    # Intentar obtener el autor o crear uno nuevo
    author_db = Author.get_or_none(Author.name == book.author.name)
    if author_db is None:
        author_db = Author.create(name=book.author.name)
    
    # Crear el libro usando el ID del autor
    
        book_db = Book_model.create(
            title=book.title,
            author=author_db.id,  # Pasar el ID del autor
            publisher=book.publisher,
            isbn=book.isbn,
            publicationYear=book.publicationYear,
            genre=book.genre,
            language=book.language,
            pageCount=book.pageCount,
            price=book.price,
            format=book.format,
            edition=book.edition,
        )
    return book_db

@book_route.get("/")
def get_book():
    books = Book_model.select().where(Book_model.id > 0).dicts()
    return list(books)

@book_route.get("/{book_id}")
def get_book(book_id: int):
    try:
        book = Book_model.get(Book_model.id == book_id)
        return book
    except Book_model.DoesNotExist:
        raise HTTPException(status_code=404, detail="Book does not exist")

@book_route.put("/{id}")
def update_book(id: int, book: BookSchema = Body(...)):
    try:
        book_update = Book_model.get(Book_model.id == id)
        book_update.title = book.title
        book_update.author = book.author
        book_update.publisher = book.publisher
        book_update.isbn = book.isbn
        book_update.publicationYear = book.publicationYear
        book_update.genre = book.genre
        book_update.language = book.language
        book_update.pageCount = book.pageCount
        book_update.price = book.price
        book_update.format = book.format
        book_update.edition = book.edition
        book_update.save()
        return {"message": f"{id} updated"}
    except Book_model.DoesNotExist:
        raise HTTPException(status_code=404, detail="Failed to update")

@book_route.delete("/{id}")
def delete_book(id: int):
    try:
        book = Book_model.get(Book_model.id == id)
        book.delete_instance()
        return {"message": f"{id} deleted"}
    except Book_model.DoesNotExist:
        raise HTTPException(status_code=404, detail="Book not found")
