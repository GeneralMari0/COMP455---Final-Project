import pandas as pd

"""
Using Pandas to find the highest rated books in each genre
Referencing: https://pandas.pydata.org/docs/user_guide/10min.html
"""

# read in the whole csv
csv_data = pd.read_csv("GoodReads_100k_books.csv")

# drop the unnecessary cols
data = csv_data.loc[:, ["author", "genre", "title", "rating", "totalratings"]]

# only consider books with at least 1 million total ratings
filtered_data = data[data["totalratings"] >= 1000000]

# since books can have multiple genres
# e.g. "Couture,Fashion,Historical,Art,Nonfiction"
# we need to split on the comma to get each genre

# dropna removes empty values
# explode splits the list of genres into individual elements
# unique removes duplicates
all_genres = filtered_data["genre"].dropna().str.split(",").explode().unique()

# print(len(all_genres))
# print(all_genres)

# this gives a list of 82 unique genres
# from which, I picked the following 10 categories:
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

# since we want at least 10 books for each category,
# we will need to lower the rating requirement,
# as some categories are less popular
filtered_data = data[data["totalratings"] >= 100000]

# write the lists out to a text file
with open("top_books_by_genre.txt", "w") as file:
    for genre in genres:

        # filter by category, and sort by ratings
        sorted = filtered_data[
            filtered_data["genre"].str.contains(genre, case=False, na=False)
        ].sort_values(by="rating", ascending=False)

        # pick the top 10 results
        result = sorted.iloc[:10][["title", "rating", "totalratings"]]

        # write out to the file
        file.write(f"Top 10 {genre} books:\n")
        # write as a string
        file.write(result.to_string(index=False))
        file.write("\n\n")
