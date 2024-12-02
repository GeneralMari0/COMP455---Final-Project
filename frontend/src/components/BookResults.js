import React from 'react';

const BookResults = ({ books }) => {
    return (
	<div className="columnContainer">
            <div className="bookResults">
                {books.length === 0 ? (
                    <p>No books found</p>
                ) : (
                    books.map((book) => (
                        <div
                            key={book.id}
                            style={{
                                border: '1px solid #ddd',
                                margin: '10px',
                                padding: '10px',
                                display: 'flex',
                            }}
                        >
                            {book.image ? (
                                <img
                                    src={book.image}
                                    alt={book.title}
                                    style={{
                                        width: '100px',
                                        height: '150px',
                                        marginRight: '10px',
                                    }}
                                />
                            ) : (
                                <div
                                    style={{
                                        width: '100px',
                                        height: '150px',
                                        marginRight: '10px',
                                        backgroundColor: '#ddd',
                                        display: 'flex',
                                        alignItems: 'center',
                                        justifyContent: 'center',
                                        color: '#555',
                                        fontSize: '12px',
                                    }}
                                >
                                    No Image
                                </div>
                            )}
                            <div className="bookEntry">
                                <h3>{book.title}</h3>
                                <p>
                                    <strong>Author:</strong> {book.author}
                                </p>
                                <p>
                                    <strong>Genre:</strong>{' '}
                                    {Array.isArray(book.genre) ? book.genre.join(', ') : book.genre}
                                </p>
                                <p>
                                    <strong>Pages:</strong> {book.pages}
                                </p>
                                <p>
                                    <strong>Rating:</strong> {book.rating}
                                </p>
                                <p>
                                    <strong>ISBN13:</strong> {book.isbn13}
                                </p>
                                <p className="description">
                                    <strong>Description:</strong> {book.description}
                                </p>
                                {book.link && (
                                    <p>
                                        <a href={book.link} target="_blank" rel="noopener noreferrer">
                                            More Info
                                        </a>
                                    </p>
                                )}
                            </div>
                        </div>
                    ))
                )}
            </div>
            <div className="recommendations">
	    	TODO: recommendations here
      	    </div>
        </div>
    );
};

export default BookResults;
