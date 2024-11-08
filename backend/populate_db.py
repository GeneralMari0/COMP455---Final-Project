from app import app, db, Book

def init_db():
    with app.app_context():
        db.create_all()
        
        # Add sample data 
        if not Book.query.first(): 
            # Sample data
            book1 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Fiction", pages=180)
            book2 = Book(title="1984", author="George Orwell", genre="Dystopian", pages=328)
            book3 = Book(title="To Kill a Mockingbird", author="Harper Lee", genre="Fiction", pages=281)

            db.session.add(book1)
            db.session.add(book2)
            db.session.add(book3)
            db.session.commit()
            print("Sample data added to the database.")
        else:
            print("Database already initialized.")

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully.")
