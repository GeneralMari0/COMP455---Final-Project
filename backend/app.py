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
    totalratings = Integer()

    class Index:
        name = 'books'

# Endpoint to get books based on filters
@app.route('/api/books', methods=['GET'])
def get_books():
    # Get filter parameters from query string
    title = request.args.get('title', '', type=str)
    author = request.args.get('author', '', type=str)
    description = request.args.get('description', '', type=str)
    isbn13 = request.args.get('isbn13', '', type=str)
    genre_list = request.args.getlist('genre')
    max_pages = request.args.get('max_pages', None, type=int)
    min_pages = request.args.get('min_pages', None, type=int)
    min_rating = request.args.get('min_rating', None, type=float)
    max_rating = request.args.get('max_rating', None, type=float)
    totalratings = request.args.get('totalratings', 0, type=int)

    # Base search
    s = Search(index='books')

    # Get top 10 books in selected genre
    r = s.filter('range', totalratings={'gte': 100000})
    if genre_list:
        for genre in genre_list:
            r = r.filter('term', genre=genre)
    r = r.sort('-rating')

    # Apply filters
    if title:
        s = s.query('match_phrase_prefix', title=title)
    if author:
        s = s.query('match_phrase_prefix', author=author)
    if description:
        s = s.query('match_phrase', description=description)
    if isbn13:
        s = s.filter('term', isbn13=isbn13)
    # Right now we match ALL genres, if we want to match ANY genres, use this code instead
    # I might make it so the user can choose ALL or ANY depending on their preference
    # But right now this should be good enough for the assignment
    # if genre_list:
    #     s = s.filter('terms', genre=genre_list)
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

    # Limit the results to 50
    s = s[:50]

    # Limit top 10 to 10
    r = r[:10]

    # Execute search and serialize results
    response = s.execute()
    top10response = r.execute()
    books = response.hits
    top10 = top10response.hits

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

    top10results = [
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
	for book in top10
    ]

    return jsonify({"books": result, "top10": top10results})

if __name__ == '__main__':
    app.run(debug=True)
