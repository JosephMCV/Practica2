"""
Module for defining database models using the Peewee ORM.
"""

import os
from dotenv import load_dotenv
from peewee import (
    Model, AutoField, CharField,
    IntegerField, DecimalField,
    ForeignKeyField, MySQLDatabase
)

load_dotenv()

database = MySQLDatabase(
    os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
)

class Camera(Model):
    """Model representing a camera."""
    id = AutoField(primary_key=True)
    cameraModel = CharField(max_length=50)
    resolution = CharField(max_length=20)
    pixels = IntegerField()
    zoom = DecimalField(max_digits=10, decimal_places=2)
    cameraMode = CharField(max_length=10)

    class Meta:
        """Class defining properties of the Camera model."""
        database = database
        table_name = "camera"

class CellphoneModel(Model):
    """Model representing a cellphone."""
    imei = IntegerField(primary_key=True)
    color = CharField(max_length=50)
    brand = CharField(max_length=50)
    model = CharField(max_length=50)
    portType = CharField(max_length=50)
    systemStorage = DecimalField(max_digits=10, decimal_places=3)
    ram = IntegerField()
    price = IntegerField()

    class Meta:
        """Class defining properties of the CellphoneModel."""
        database = database
        table_name = "cellphone"

class Author(Model):
    """Model representing an author."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)

    class Meta:
        """Class defining properties of the Author model."""
        database = database
        table_name = "author"

class BookModel(Model):
    """Model representing a book."""
    id = AutoField(primary_key=True)
    title = CharField(max_length=20)
    publisher = CharField(max_length=20)
    isbn = CharField(max_length=10)
    publicationYear = IntegerField()
    genre = CharField(max_length=10)
    language = CharField(max_length=20)
    pageCount = IntegerField()
    price = DecimalField(max_digits=10, decimal_places=3)
    bookFormat = CharField(max_length=20)
    edition = CharField(max_length=20)

    class Meta:
        """Class defining properties of the BookModel."""
        database = database
        table_name = "book"

class AuthorBook(Model):
    """Model representing the relationship between authors and books."""
    author = ForeignKeyField(Author, backref="books")
    book = ForeignKeyField(BookModel, backref="authors")

    class Meta:
        """Class defining properties of the AuthorBook model."""
        database = database
        table_name = "author_book"

class CameraCellphone(Model):
    """Model representing the relationship between cameras and cellphones."""
    camera = ForeignKeyField(Camera, backref="cellphones")
    cellphone = ForeignKeyField(CellphoneModel, backref="cameras")

    class Meta:
        """Class defining properties of the CameraCellphone model."""
        database = database
        table_name = "camera_cellphone"
        