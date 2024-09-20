"""Book routes for the FastAPI application."""

from fastapi import APIRouter, Body, HTTPException
from models.book_schema import BookModel as BookSchema
from database import BookModel, AuthorBook

book_route = APIRouter()

@book_route.post("/")
def create_book(book: BookSchema = Body(...)):
    """Create a new book with the associated authors."""
    book_db = BookModel.create(
        title=book.title,
        publisher=book.publisher,
        isbn=book.isbn,
        publicationYear=book.publicationYear,
        genre=book.genre,
        language=book.language,
        pageCount=book.pageCount,
        price=book.price,
        format=book.bookFormat,
        edition=book.edition,
    )
    for author_id in book.author:
        AuthorBook.create(
            author=author_id,
            book=book_db.id
        )
    return {"message": "Book created successfully"}

@book_route.get("/")
def get_books():
    """Retrieve all books."""
    books = BookModel.select().where(BookModel.id > 0).dicts()
    return list(books)

@book_route.get("/{book_id}")
def get_book(book_id: int):
    """Retrieve a specific book by ID."""
    try:
        book = BookModel.get(BookModel.id == book_id)
        return book
    except BookModel.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Book does not exist") from exc

@book_route.put("/{book_id}")
def update_book(book_id: int, book: BookSchema = Body(...)):
    """Update an existing book."""
    try:
        book_update = BookModel.get(BookModel.id == book_id)
        book_update.title = book.title
        book_update.author = book.author
        book_update.publisher = book.publisher
        book_update.isbn = book.isbn
        book_update.publicationYear = book.publicationYear
        book_update.genre = book.genre
        book_update.language = book.language
        book_update.pageCount = book.pageCount
        book_update.price = book.price
        book_update.bookFormat = book.bookFormat
        book_update.edition = book.edition
        book_update.save()
        return {"message": f"Book with ID {book_id} updated"}
    except BookModel.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Failed to update") from exc

@book_route.delete("/{book_id}")
def delete_book(book_id: int):
    """Delete a book by ID."""
    try:
        bookauthor = AuthorBook.get(AuthorBook.book == book_id)
        bookauthor.delete.instance()
        book = BookModel.get(BookModel.id == book_id)
        book.delete_instance()
        return {"message": f"Book with ID {book_id} deleted"}
    except BookModel.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Book not found") from exc