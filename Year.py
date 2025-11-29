books = [
    {"id": 1, "title": "A Great Read", "author": "Alice", "Year" : 1979},
    {"id": 2, "title": "Code Secrets", "author": "Bob", "Year" : 2002},
    {"id": 3, "title": "The Third Way", "author": "Charlie", "Year" : 2017},
] 
@app.post("/books")
def add_book(book: dict):
    global counter
    new_book = {
        "id": counter,
        "title": book.get("title"),
        "author": book.get("author"),
       "Year":book.get("Year")
    }
    books.append(new_book)
    counter += 1
    return new_book
