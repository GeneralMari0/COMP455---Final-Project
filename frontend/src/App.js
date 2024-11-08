// src/App.js
import React, { useState } from 'react';
import axios from 'axios';
import SearchPanel from './components/SearchPanel';
import BookResults from './components/BookResults';

const App = () => {
    const [books, setBooks] = useState([]);

    const getBooks = async (filters) => {
        try {
            const params = {};
            if (filters.title) params.title = filters.title;
            if (filters.author) params.author = filters.author;
            if (filters.minPages) params.min_pages = filters.minPages;
            if (filters.maxPages) params.max_pages = filters.maxPages;
            if (filters.genre) params.genre = filters.genre;

            const response = await axios.get('http://127.0.0.1:5000/api/books', { params });
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
