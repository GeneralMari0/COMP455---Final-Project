import React, { useState } from 'react';

const SearchPanel = ({ onSearch }) => {
    const [title, setTitle] = useState('');
    const [author, setAuthor] = useState('');
    const [description, setDescription] = useState('');
    const [isbn13, setIsbn13] = useState('');
    const [minPages, setMinPages] = useState('');
    const [maxPages, setMaxPages] = useState('');
    const [minRating, setMinRating] = useState('');
    const [maxRating, setMaxRating] = useState('');
    const [selectedGenres, setSelectedGenres] = useState([]);

    const genres = [
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
    ];

    const handleSubmit = (e) => {
        e.preventDefault();
        onSearch({
            title,
            author,
            description,
            isbn13,
            minPages,
            maxPages,
            minRating,
            maxRating,
            genre: selectedGenres,
        });
    };

    const handleGenreChange = (e) => {
        const { value, checked } = e.target;
        if (checked) {
            setSelectedGenres([...selectedGenres, value]);
        } else {
            setSelectedGenres(selectedGenres.filter((g) => g !== value));
        }
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
                type="text"
                placeholder="Description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            />
            <input
                type="text"
                placeholder="ISBN13"
                value={isbn13}
                onChange={(e) => setIsbn13(e.target.value)}
            />
            <input
                type="number"
		min="0"
                placeholder="Min Pages"
                value={minPages}
                onChange={(e) => setMinPages(e.target.value)}
            />
            <input
                type="number"
                placeholder="Max Pages"
		min="1"
                value={maxPages}
                onChange={(e) => setMaxPages(e.target.value)}
            />
            <input
                type="number"
                step="0.1"
		min="0.0"
		max="5.0"
                placeholder="Min Rating"
                value={minRating}
                onChange={(e) => setMinRating(e.target.value)}
            />
            <input
                type="number"
                step="0.1"
		min="0.0"
		max="5.0"
                placeholder="Max Rating"
                value={maxRating}
                onChange={(e) => setMaxRating(e.target.value)}
            />
            <div>
                <label><strong>Genres:</strong></label>
                {genres.map((genre) => (
                    <div key={genre}>
                        <input
                            type="checkbox"
                            value={genre}
                            checked={selectedGenres.includes(genre)}
                            onChange={handleGenreChange}
                        />
                        <label>{genre}</label>
                    </div>
                ))}
            </div>
            <button type="submit">Search</button>
        </form>
    );
};

export default SearchPanel;
