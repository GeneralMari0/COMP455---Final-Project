import json
import os

from elasticsearch import Elasticsearch
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure Elasticsearch
ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST", "localhost")
ELASTICSEARCH_PORT = os.getenv("ELASTICSEARCH_PORT", "9200")

es = Elasticsearch([f"http://{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}"])

# Index name for books
BOOKS_INDEX = "books"

# Enhanced mapping for all fields
BOOKS_MAPPING = {
    "mappings": {
        "properties": {
            "author": {
                "type": "text",
                "analyzer": "standard",
                "fields": {"keyword": {"type": "keyword"}},
            },
            "bookformat": {"type": "keyword"},
            "desc": {"type": "text", "analyzer": "standard"},
            "genre": {
                "type": "text",
                "analyzer": "standard",
                "fields": {"keyword": {"type": "keyword"}},
            },
            "img": {"type": "keyword"},
            "isbn": {"type": "keyword"},
            "isbn13": {"type": "keyword"},
            "link": {"type": "keyword"},
            "pages": {"type": "integer"},
            "rating": {"type": "float"},
            "reviews": {"type": "integer"},
            "title": {
                "type": "text",
                "analyzer": "standard",
                "fields": {"keyword": {"type": "keyword"}},
            },
            "totalratings": {"type": "integer"},
        }
    },
    "settings": {"analysis": {"analyzer": {"standard": {"type": "standard"}}}},
}


def create_index():
    """Create the books index if it doesn't exist"""
    if not es.indices.exists(index=BOOKS_INDEX):
        es.indices.create(index=BOOKS_INDEX, body=BOOKS_MAPPING)


def load_sample_data(file_path):
    """Load sample data from JSON file into Elasticsearch"""
    with open(file_path, "r", encoding="utf-8") as file:
        books = json.load(file)

    for book in books:
        # Clean empty strings to None
        for key, value in book.items():
            if value == "":
                book[key] = None

        # Convert string numbers to actual numbers
        if book.get("pages"):
            book["pages"] = int(book["pages"])
        if book.get("rating"):
            book["rating"] = float(book["rating"])
        if book.get("reviews"):
            book["reviews"] = int(book["reviews"])
        if book.get("totalratings"):
            book["totalratings"] = int(book["totalratings"])

        es.index(index=BOOKS_INDEX, document=book)

    # Refresh the index to make the documents searchable immediately
    es.indices.refresh(index=BOOKS_INDEX)


@app.route("/api/books", methods=["GET"])
def get_books():
    # Get search parameters from query string
    search_params = {}
    for param in request.args:
        if request.args.get(param):
            search_params[param] = request.args.get(param)

    # Build query
    must_conditions = []

    for field, value in search_params.items():
        if field in ["pages", "rating", "reviews", "totalratings"]:
            # Handle numeric range queries
            try:
                if field == "rating":
                    value = float(value)
                else:
                    value = int(value)
                must_conditions.append({"range": {field: {"gte": value}}})
            except ValueError:
                continue
        elif field in ["bookformat", "isbn", "isbn13"]:
            # Exact match for these fields
            must_conditions.append({"term": {field: value}})
        else:
            # Fuzzy text search for other fields
            must_conditions.append(
                {"match": {field: {"query": value, "fuzziness": "AUTO"}}}
            )

    # Construct the final query
    query = {
        "query": {
            "bool": {
                "must": must_conditions if must_conditions else [{"match_all": {}}]
            }
        },
        "size": 100,
    }

    # Execute search
    try:
        response = es.search(index=BOOKS_INDEX, body=query)
        hits = response["hits"]["hits"]
        books = [{"id": hit["_id"], **hit["_source"]} for hit in hits]
        return jsonify(books)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Command-line setup
if __name__ == "__main__":
    # Create index and load sample data if specified
    create_index()

    # Check if sample data should be loaded
    if os.getenv("LOAD_SAMPLE_DATA"):
        sample_data_path = os.getenv("SAMPLE_DATA_PATH", "sample.json")
        if os.path.exists(sample_data_path):
            print(f"Loading sample data from {sample_data_path}")
            load_sample_data(sample_data_path)
            print("Sample data loaded successfully")

    app.run(debug=True)
