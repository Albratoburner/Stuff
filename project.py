from fastapi import FastAPI, Depends
from database import get_db, engine
from sqlalchemy.orm import Session
import Model
from pydantic import BaseModel

app = FastAPI()

class Bookstore(BaseModel):
    id: int
    title: str
    author: str
    publish_date: str

@app.post("/books")
def create_books(book: Bookstore, db: Session = Depends(get_db)):
    new_book = Model.Book(id = book.id, title = book.title, author = book.author, publish_date = book.publish_date)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.get("/books")
def create_books(db: Session = Depends(get_db)):
    books = db.query(Model.Book).all()
    return books 

