"""Author routes for the FastAPI application."""

from fastapi import APIRouter, Body, HTTPException
from models.book_schema import Author as AuthorSchema
from database import Author, AuthorBook

author_router = APIRouter()

@author_router.post("/")
def create_author(author: AuthorSchema = Body(...)):
    """Create a new author."""
    Author.create(id=author.id, name=author.name)
    return {"message": "Author created successfully"}

@author_router.get("/")
def get_authors():
    """Retrieve all authors."""
    authors = Author.select().where(Author.id > 0).dicts()
    return list(authors)

# pylint: disable=no-member
@author_router.get("/{author_id}")
def get_author(author_id: int):
    """Retrieve a specific author by ID."""
    try:
        author = Author.get(Author.id == author_id)
        return author
    except Author.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Author does not exist") from exc

@author_router.put("/{author_id}")
def update_author(author_id: int, author: AuthorSchema = Body(...)):
    """Update an existing author."""
    try:
        author_update = Author.get(Author.id == author_id)
        author_update.name = author.name
        author_update.save()
        return {"message": f"Author with ID {author_id} updated"}
    except Author.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Failed to update") from exc

@author_router.delete("/{author_id}")
def delete_author(author_id: int):
    """Delete an author by ID."""
    try:
        book_author = AuthorBook.get(AuthorBook.book == author_id)
        book_author.delete.instance()
        author = Author.get(Author.id == author_id)
        author.delete_instance()
        return {"message": f"Author with ID {author_id} deleted"}
    except Author.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Author not found") from exc
    