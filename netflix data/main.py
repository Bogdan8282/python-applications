# Pandas lib required to run this code
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
netflix_df = pd.read_csv("netflix_data.csv")

# Filter to remove TV shows
netflix_subset = netflix_df[netflix_df['type'] != 'TV Show']

# Create a DataFrame netflix_movies with specific columns
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]

# Filter for movies shorter than 60 minutes
short_movies = netflix_movies[netflix_movies["duration"] < 60]

# Assign colors based on genre groups
colors = []
for genre in netflix_movies["genre"]:
    if "Children" in genre:
        colors.append("blue")
    elif "Documentaries" in genre:
        colors.append("green")
    elif "Stand-Up" in genre:
        colors.append("red")
    else:
        colors.append("gray")

# Create a plot
fig, ax = plt.subplots()
ax.scatter(netflix_movies["release_year"], netflix_movies["duration"], c=colors)
ax.set_xlabel("Release year")
ax.set_ylabel("Duration (min)")
ax.set_title("Movie Duration by Year of Release")
plt.show() 