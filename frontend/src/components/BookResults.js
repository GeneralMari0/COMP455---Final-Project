import React from 'react';

const BookResults = ({ books }) => {
    if (books.length === 0) {
	return (<div><p>Try searching!</p></div>)
    } else {
        return (
       	    <div className="columnContainer">
                <div className="bookResults">
		    <h3>Results</h3>
                    {books.books.length === 0 ? (
                        <p>No books found</p>
                    ) : (
                        books.books.map((book) => (
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
		    <h3>Best similar books</h3>
	 	    {books.top10.length === 0 ? (
                        <p>No recommendations found</p>
                    ) : (
                        books.top10.map((book) => (
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
                                <div className="recommendation">
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
            </div>
        );
    }
};

export default BookResults;
