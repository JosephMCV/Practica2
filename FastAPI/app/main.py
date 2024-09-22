"""
Main application module for the FastAPI project.

This module sets up the FastAPI application, manages the database connection
and table creation, and includes the route definitions.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import (database as connection, Camera, CellphoneModel, Author,
                        BookModel,CameraCellphone,AuthorBook)
from routes.book_routes import book_route
from routes.cellphone_routes import cellphone_route
from routes.camera_routes import camera_route
from routes.author_routes import author_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager for the application's lifespan.

    Connects to the database, creates tables if needed, and ensures
    proper closure of the database connection on shutdown.
    """
    if connection.is_closed():
        connection.connect()
        connection.create_tables([
            Camera, CellphoneModel, Author, BookModel,CameraCellphone,AuthorBook
        ])

    try:
        yield
    finally:
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan=lifespan)

app.include_router(book_route, prefix="/api/books", tags=["books"])
app.include_router(cellphone_route, prefix="/api/cellphones", tags=["cellphones"])
app.include_router(camera_route, prefix="/api/cameras", tags=["cameras"])
app.include_router(author_router, prefix="/api/authors", tags=["authors"])
