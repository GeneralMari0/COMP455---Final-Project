from app import app, Book
from elasticsearch_dsl import connections

def init_es():
    # Connect to Elasticsearch
    connections.create_connection(hosts=['http://localhost:9200'])

    # Initialize the index
    if not Book._index.exists():
        Book.init()
        print("Created Elasticsearch index 'books'.")
    else:
        print("Elasticsearch index 'books' already exists.")

    # Check if the index is empty
    s = Book.search()
    response = s.execute()
    if len(response.hits) == 0:
        # Add sample data
        book1 = Book(meta={'id': 1}, title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Fiction", pages=180)
        book2 = Book(meta={'id': 2}, title="1984", author="George Orwell", genre="Dystopian", pages=328)
        book3 = Book(meta={'id': 3}, title="To Kill a Mockingbird", author="Harper Lee", genre="Fiction", pages=281)

        book1.save()
        book2.save()
        book3.save()

        print("Sample data added to Elasticsearch index.")
    else:
        print("Elasticsearch index already contains data.")

if __name__ == '__main__':
    init_es()
    print("Elasticsearch initialized successfully.")
