from pydantic import BaseModel,StrictStr,validator

class Author(BaseModel):
    name:str

class Book_model(BaseModel):
    
    id:int
    title:str
    author:Author
    publisher: str
    isbn: str
    publicationYear: int
    genre: str
    language: str
    pageCount: int
    price: float
    format: str
    edition: str


    @validator("publicationYear")
    def year_cant_be_negative(cls,v):
        if v < 0:
            raise ValueError("Year of publication cant be negative")
        return v
    
    @validator("pageCount")
    def genre(cls,v):
        if v < 0:
            raise ValueError("The pages of the book cant be negative")
        return v
    
   

   