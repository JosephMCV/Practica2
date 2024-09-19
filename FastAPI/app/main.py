from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import database as connection
from database import *
from routes.book_routes import book_route
from routes.cellphone_routes import cellphone_route
from routes.camera_routes import camera_route
from routes.author_routes import author_route

@asynccontextmanager
async def lifespan(app: FastAPI):

    if connection.is_closed():
        connection.connect()
        connection.create_tables([Camera, Cellphone_model, Author, Book_model, Author_Book,Camera_Cellphone])

    try:
        yield
    
    finally:
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan = lifespan)

app.include_router(book_route, prefix="/api/books", tags={"books"})
app.include_router(cellphone_route, prefix="/api/cellphones", tags={"cellphones"})
app.include_router(camera_route, prefix="/api/cameras", tags={"cameras"})
app.include_router(author_route, prefix="/api/authors", tags={"authors"})
