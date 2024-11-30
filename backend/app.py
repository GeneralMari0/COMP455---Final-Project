from flask import Flask, jsonify, request
from flask_cors import CORS
from elasticsearch_dsl import Document, Text, Integer, Search, connections, Float, Keyword

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests (separate frontend)

# Connect to Elasticsearch
connections.create_connection(hosts=['http://localhost:9200'])

# Book model
class Book(Document):
    title = Text()
    author = Text()
    genre = Keyword()
    pages = Integer()
    description = Text()
    image = Text()
    isbn13 = Text()
    link = Text()
    rating = Float()

    class Index:
        name = 'books'

# Endpoint to get books based on filters
@app.route('/api/books', methods=['GET'])
def get_books():
    # Get filter parameters from query string
    title = request.args.get('title', '', type=str)
    author = request.args.get('author', '', type=str)
    genre_list = request.args.getlist('genre')
    max_pages = request.args.get('max_pages', None, type=int)
    min_pages = request.args.get('min_pages', None, type=int)
    min_rating = request.args.get('min_rating', None, type=float)
    max_rating = request.args.get('max_rating', None, type=float)

    # Base search
    s = Search(index='books')

    # Apply filters
    if title:
        s = s.query('match_phrase_prefix', title=title)
    if author:
        s = s.query('match_phrase_prefix', author=author)
    if genre_list:
        for genre in genre_list:
            s = s.filter('term', genre=genre)
    if max_pages is not None or min_pages is not None:
        page_range = {}
        if min_pages is not None:
            page_range['gte'] = min_pages
        if max_pages is not None:
            page_range['lte'] = max_pages
        s = s.filter('range', pages=page_range)
    if min_rating is not None or max_rating is not None:
        rating_range = {}
        if min_rating is not None:
            rating_range['gte'] = min_rating
        if max_rating is not None:
            rating_range['lte'] = max_rating
        s = s.filter('range', rating=rating_range)

    # Limit the results to 100
    s = s[:100]

    # Execute search and serialize results
    response = s.execute()
    books = response.hits

    result = [
        {
            "id": book.meta.id,
            "title": book.title,
            "author": book.author,
            "genre": list(book.genre),
            "pages": book.pages,
            "description": book.description,
            "image": book.image,
            "isbn13": book.isbn13,
            "link": book.link,
            "rating": book.rating
        }
        for book in books
    ]

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
