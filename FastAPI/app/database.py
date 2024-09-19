from dotenv import load_dotenv
from peewee import *
import os

load_dotenv()

database = MySQLDatabase(
    os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
)

class Camera(Model):
    id = AutoField(primary_key = True)
    cameraModel = CharField(max_length=50)
    resolution = CharField(max_length=20)
    pixels = IntegerField()
    zoom = DecimalField(max_digits=10,decimal_places=2)
    camera_mode= CharField(max_length=10)

    class Meta:
        database = database
        table_name = "camera"

class Cellphone_model(Model):
    imei = IntegerField(primary_key = True)
    color = CharField(max_length=50)
    brand = CharField(max_length=50)
    model = CharField(max_length=50)
    port_type = CharField(max_length=50)
    system_storage = DecimalField(max_digits=10,decimal_places=3)
    ram = IntegerField()
    price = IntegerField()

    class Meta:
        database = database
        table_name = "cellphone"


class Author(Model):
    id = AutoField(primary_key = True)
    name = CharField(max_length=50)
    

    class Meta:
        database = database
        table_name = "author"

class Book_model(Model):
    id = AutoField(primary_key = True)
    title = CharField(max_length=20)
    publisher = CharField(max_length=20)
    isbn= CharField(max_length=10)
    publicationYear = IntegerField()
    genre = CharField(max_length=10)
    language = CharField(max_length=20)
    pageCount = IntegerField()
    price = DecimalField(max_digits=10,decimal_places=3)
    format = CharField(max_length=20)
    edition = CharField(max_length=20)

    class Meta:
        database = database
        table_name = "book"

class Author_Book(Model):
    author = ForeignKeyField(Author,backref="books")
    book = ForeignKeyField(Book_model, backref="authors")

    class Meta:
        database = database
        table_name = "author_book"

class Camera_Cellphone(Model):
    camera = ForeignKeyField(Camera,backref="cellphones")
    cellphone = ForeignKeyField(Cellphone_model,backref="cameras")
    
    class Meta:
        database = database
        table_name = "camera_cellphone"
