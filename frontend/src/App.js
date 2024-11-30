import React, { useState } from 'react';
import axios from 'axios';
import SearchPanel from './components/SearchPanel';
import BookResults from './components/BookResults';
import qs from 'qs';

const App = () => {
    const [books, setBooks] = useState([]);

    const getBooks = async (filters) => {
        try {
            const params = {};
            if (filters.title) params.title = filters.title;
            if (filters.author) params.author = filters.author;
            if (filters.description) params.description = filters.description;
            if (filters.isbn13) params.isbn13 = filters.isbn13;
            if (filters.minPages) params.min_pages = filters.minPages;
            if (filters.maxPages) params.max_pages = filters.maxPages;
            if (filters.minRating) params.min_rating = filters.minRating;
            if (filters.maxRating) params.max_rating = filters.maxRating;
            if (filters.genre && filters.genre.length > 0) {
                params.genre = filters.genre;
            }

            const response = await axios.get('http://127.0.0.1:5000/api/books', {
                params: params,
                paramsSerializer: params => {
                    // Need to use qs to serialize parameters
                    // https://stackoverflow.com/questions/49944387/how-to-correctly-use-axios-params-with-arrays
                    return qs.stringify(params, { arrayFormat: 'repeat' });
                }
            });
            setBooks(response.data);
        } catch (error) {
            console.error('Error getting books:', error);
        }
    };

    return (
        <div style={{ padding: '20px' }}>
            <h1>Book Search</h1>
            <SearchPanel onSearch={getBooks} />
            <BookResults books={books} />
        </div>
    );
};

export default App;
