from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests (separate frontend)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

db = SQLAlchemy(app)

# Book model 
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    pages = db.Column(db.Integer, nullable=False)

# Endpoint to get books based on filters
@app.route('/api/books', methods=['GET'])
def get_books():
    # Get filter parameters from query string
    title = request.args.get('title', '', type=str)
    author = request.args.get('author', '', type=str)
    genre = request.args.get('genre', '', type=str)
    max_pages = request.args.get('max_pages', None, type=int)
    min_pages = request.args.get('min_pages', None, type=int)

    # Base query
    query = Book.query

    # Apply filters
    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    if genre:
        query = query.filter(Book.genre == genre)
    if max_pages is not None:
        query = query.filter(Book.pages <= max_pages)
    if min_pages is not None:
        query = query.filter(Book.pages >= min_pages)

    # Limit the results to 100 
    # (maybe do pagination instead? might be unnecessarily complicated for this project idk)
    query = query.limit(100)

    # Execute query and serialize results
    books = query.all()
    result = [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "pages": book.pages
        }
        for book in books
    ]

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
