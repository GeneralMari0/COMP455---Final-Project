from flask import Flask, jsonify, request
from flask_cors import CORS
from elasticsearch_dsl import Document, Text, Integer, Search, connections

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests (separate frontend)

# Connect to Elasticsearch
connections.create_connection(hosts=['http://localhost:9200'])

# Book model
class Book(Document):
    title = Text()
    author = Text()
    genre = Text()
    pages = Integer()

    class Index:
        name = 'books'

# Endpoint to get books based on filters
@app.route('/api/books', methods=['GET'])
def get_books():
    # Get filter parameters from query string
    title = request.args.get('title', '', type=str)
    author = request.args.get('author', '', type=str)
    genre = request.args.get('genre', '', type=str)
    max_pages = request.args.get('max_pages', None, type=int)
    min_pages = request.args.get('min_pages', None, type=int)

    # Base search
    s = Search(index='books')

    # Apply filters
    if title:
        s = s.query('match_phrase_prefix', title=title)
    if author:
        s = s.query('match_phrase_prefix', author=author)
    if genre:
        s = s.filter('term', genre=genre)
    if max_pages is not None or min_pages is not None:
        page_range = {}
        if min_pages is not None:
            page_range['gte'] = min_pages
        if max_pages is not None:
            page_range['lte'] = max_pages
        s = s.filter('range', pages=page_range)

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
            "genre": book.genre,
            "pages": book.pages
        }
        for book in books
    ]

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
