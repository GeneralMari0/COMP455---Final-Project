import React from 'react';

const BookResults = ({ books }) => {
    return (
        <div>
            {books.length === 0 ? (
                <p>No books found</p>
            ) : (
                books.map((book) => (
                    <div key={book.id} style={{ border: '1px solid #ddd', margin: '10px', padding: '10px' }}>
                        <h3>{book.title}</h3>
                        <p><strong>Author:</strong> {book.author}</p>
                        <p><strong>Genre:</strong> {book.genre}</p>
                        <p><strong>Pages:</strong> {book.pages}</p>
                    </div>
                ))
            )}
        </div>
    );
};

export default BookResults;
