from fastapi import APIRouter, Body, HTTPException
from models.book_schema import Author as AuthorSchema
from database import  Author

author_route = APIRouter()

@author_route.post("/")
def create_shirts(author: AuthorSchema = Body(...)):
    Author.create(id = author.id, name = author.name)
    return {"message": "Author created successfully"}

@author_route.get("/")
def get_author():
    author = Author.select().where(Author.id > 0).dicts()
    return list(author)

@author_route.get("/{author_id}")
def get_author(author_id: int):
    try:
        author = Author.get(Author.id == author_id)
        return author
    except Author.DoesNotExist:
        raise HTTPException(status_code=404, detail="Book does not exist")

@author_route.put("/{id}")
def update_author(id: int, author: AuthorSchema = Body(...)):
    try:
        author_update = Author.get(Author.id == id)
        author_update.name = author.name
        author_update.author = author.book
        author_update.save()
        return {"message": f"{id} updated"}
    except Author.DoesNotExist:
        raise HTTPException(status_code=404, detail="Failed to update")

@author_route.delete("/{id}")
def delete_author(id: int):
    try:
        author = Author.get(Author.id == id)
        author.delete_instance()
        return {"message": f"{id} deleted"}
    except AuthorSchema.DoesNotExist:
        raise HTTPException(status_code=404, detail="Book not found")
