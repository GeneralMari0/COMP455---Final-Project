import React, { useState } from 'react';

const SearchPanel = ({ onSearch }) => {
    const [title, setTitle] = useState('');
    const [author, setAuthor] = useState('');
    const [minPages, setMinPages] = useState('');
    const [maxPages, setMaxPages] = useState('');
    const [genre, setGenre] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onSearch({ title, author, minPages, maxPages, genre });
    };

    return (
        <form onSubmit={handleSubmit} style={{ marginBottom: '20px' }}>
            <input
                type="text"
                placeholder="Title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
            />
            <input
                type="text"
                placeholder="Author"
                value={author}
                onChange={(e) => setAuthor(e.target.value)}
            />
            <input
                type="number"
                placeholder="Min Pages"
                value={minPages}
                onChange={(e) => setMinPages(e.target.value)}
            />
            <input
                type="number"
                placeholder="Max Pages"
                value={maxPages}
                onChange={(e) => setMaxPages(e.target.value)}
            />
            <input
                type="text"
                placeholder="Genre"
                value={genre}
                onChange={(e) => setGenre(e.target.value)}
            />
            <button type="submit">Search</button>
        </form>
    );
};

export default SearchPanel;
