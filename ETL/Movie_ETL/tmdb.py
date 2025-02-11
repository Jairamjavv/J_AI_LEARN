import os
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["API_KEY"]
access_token = os.environ["ACCESS_TOKEN"]
tmdb_url = os.environ["TMDB_URL"]

# Extract
movies_url = f"{tmdb_url}discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
genres_url = f"{tmdb_url}genre/movie/list?language=en"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {access_token}",
}

movies_response = requests.get(movies_url, headers=headers).json()
genres_response = requests.get(genres_url, headers=headers).json()

# Extract to a pandas DataFrame
movies_df = pd.DataFrame.from_dict(movies_response["results"])
genres_df = pd.DataFrame.from_dict(genres_response["genres"])

# Transform - filtering out the columns needed
# id, title, release_date, vote_average, vote_count, original_language, genre_ids
columns_needed = [
    "id",
    "title",
    "release_date",
    "original_language",
    "overview",
    "popularity",
    "genre_ids",
    "vote_average",
    "vote_count",
]

s = movies_df["genre_ids"].explode()
movies_df = movies_df.join(pd.crosstab(s.index, s))
print(movies_df.columns)
print(movies_df[columns_needed].head(2))

# Load
movies_df.to_csv("complete_movies_details.csv", index=False)
movies_df[columns_needed].to_csv("essential_movies_details.csv", index=False)
