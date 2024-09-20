"""
Schema models for books and authors using Pydantic.
"""

from typing import List
from pydantic import BaseModel, validator

class Author(BaseModel):
    """
    Represents an author with an ID and a name.
    """
    id: int
    name: str

class BookModel(BaseModel):
    """
    Represents a book with various attributes such as title, author, publisher, etc.
    """
    id: int
    title: str
    author: List[int]
    publisher: str
    isbn: str
    publicationYear: int
    genre: str
    language: str
    pageCount: int
    price: float
    bookFormat: str
    edition: str

    @validator("publicationYear")
    def year_cant_be_negative(cls, v):  # pylint: disable=no-self-argument
        """
        Validates that the publication year is not negative.
        
        Args:
        v (int): The publication year.

        Returns:
            int: The validated publication year.
        
        Raises:
            ValueError: If the publication year is negative.
        """
        if v < 0:
            raise ValueError("Year of publication can't be negative")
        return v

    @validator("pageCount")
    def page_count_cant_be_negative(cls, v):  # pylint: disable=no-self-argument
        """
        Validates that the page count is not negative.
        
        Args:
        v (int): The page count.

        Returns:
            int: The validated page count.
        
        Raises:
            ValueError: If the page count is negative.
        """
        if v < 0:
            raise ValueError("The pages of the book can't be negative")
        return v
   