import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "title": ["Matrix", "Inception", "Titanic", "Avatar", "Interstellar"],
    "genre": ["Action Sci-Fi", "Action Sci-Fi", "Romance Drama", "Action Adventure", "Sci-Fi Adventure"]
}

df = pd.DataFrame(data)

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df["genre"])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend(movie):
    if movie not in df["title"].values:
        return "Movie not found."
    idx = df[df["title"] == movie].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_movies = [df["title"][i[0]] for i in sim_scores[1:3]]
    return top_movies

movie = input("Enter a movie name: ")
print("Recommended Movies:", recommend(movie))
