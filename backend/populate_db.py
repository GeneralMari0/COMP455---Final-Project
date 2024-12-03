from app import app, Book
from elasticsearch_dsl import connections
import csv
import os
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch

def init_es():
    # Connect to Elasticsearch
    connections.create_connection(hosts=['http://localhost:9200'])
    es = Elasticsearch(hosts=['http://localhost:9200'])

    # Initialize the index
    if not Book._index.exists():
        Book.init()
        print("Created Elasticsearch index 'books'.")
    else:
        print("Elasticsearch index already exists. Deleting and recreating the index...")
        Book._index.delete()
        Book.init()
        print("Recreated Elasticsearch index 'books'")

    # Get the paths of the dataset
    csv_directory = os.path.join('.', 'dataset')
    csv_files = [f for f in os.listdir(csv_directory) if f.endswith('.csv')]

    # Original dataset has 82 genres, we reduce to these 10 genres to simplify the interface
    genres = [
        "Fantasy",
        "Adventure",
        "Romance",
        "Historical",
        "Academic",
        "Horror",
        "Mystery",
        "Crime",
        "Nonfiction",
        "Fiction",
    ]

    for csv_file in csv_files:
        csv_path = os.path.join(csv_directory, csv_file)

        actions = []

        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    # Extract required fields
                    author = row.get('author', '')
                    title = row.get('title', '')
                    desc = row.get('desc', '')
                    genre = row.get('genre', '')
                    # Split the comma-separated genre string into a list
                    genres_list = [g.strip() for g in genre.split(',')] if genre else []
                    # Filter genres by list above
                    genres_list = [g for g in genres_list if g in genres]
                    # Remove duplicates (Many books in the original dataset have duplicated genres for some reason)
                    genres_list = list(set(genres_list))
                    img = row.get('img', '')
                    isbn13 = row.get('isbn13', '')
                    link = row.get('link', '')
                    pages = int(float(row['pages'])) if row.get('pages') else 0
                    rating = float(row['rating']) if row.get('rating') else 0.0
                    totalratings = int(row['totalratings']) if row.get('totalratings') else 0

                    # Prepare the action for bulk indexing
                    # https://www.geeksforgeeks.org/bulk-indexing-for-efficient-data-ingestion-in-elasticsearch/#
                    action = {
                        '_op_type': 'index',
                        '_index': 'books',
                        '_source': {
                            'title': title,
                            'author': author,
                            'description': desc,
                            'genre': genres_list,
                            'image': img,
                            'isbn13': isbn13,
                            'link': link,
                            'pages': pages,
                            'rating': rating,
			                'totalratings': totalratings
                        }
                    }
                    actions.append(action)

                    # Bulk index every 5000 records
                    if len(actions) >= 5000:
                        bulk(es, actions)
                        actions = []  # Reset the list after bulk indexing
                        print(f"Indexed 5000 records from {csv_file}")

                except Exception as e:
                    print(f"Exception: {e}")
                    continue

        # Index any remaining actions
        if actions:
            bulk(es, actions)
            print(f"Indexed remaining records from {csv_file}")

    print("All books from all csv files have been added to Elasticsearch index.")

if __name__ == '__main__':
    init_es()
    print("Elasticsearch initialized successfully.")
