# Music Artist Similarity Analysis

import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer, MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (corrected filename)
df = pd.read_csv("dataset.csv")  # Dataset from Kaggle: Spotify Million Song Dataset

# --- Step 1: Basic Cleaning ---
# Drop missing values
features_to_use = ['artists', 'track_genre', 'popularity', 'danceability', 'energy', 'valence', 'speechiness', 'acousticness']
df = df[features_to_use].dropna()

# Standardize genre entries
df['track_genre'] = df['track_genre'].apply(lambda x: [x] if isinstance(x, str) else [])

# Group by artist and average numerical features
numerical_features = ['popularity', 'danceability', 'energy', 'valence', 'speechiness', 'acousticness']
artist_grouped = df.groupby('artists')[numerical_features].mean().reset_index()

# Combine genres per artist
genre_dict = df.groupby('artists')['track_genre'].sum().apply(lambda x: list(set(x)))
artist_grouped['track_genre'] = artist_grouped['artists'].map(genre_dict)

# --- Step 2: Encode Genres ---
mlb = MultiLabelBinarizer()
genres_encoded = mlb.fit_transform(artist_grouped['track_genre'])
genres_df = pd.DataFrame(genres_encoded, columns=mlb.classes_)

# Merge genre encodings with numerical features
artist_final = pd.concat([artist_grouped.drop('track_genre', axis=1), genres_df], axis=1)

# --- Step 3: Normalize Numerical Features ---
scaler = MinMaxScaler()
artist_final[numerical_features] = scaler.fit_transform(artist_final[numerical_features])

# --- Step 4: Compute Similarity ---
# Create feature matrix
feature_matrix = artist_final.drop('artists', axis=1).values
cos_sim = cosine_similarity(feature_matrix)

# --- Step 5: Find Top Matches and Plot Bar Graph ---
def get_top_matches(query_artist, top_n=10):
    try:
        idx = artist_final[artist_final['artists'].str.lower() == query_artist.lower()].index[0]
    except IndexError:
        print(f"Artist '{query_artist}' not found.")
        return None

    similarity_scores = list(enumerate(cos_sim[idx]))
    similarity_scores = [(i, score) for i, score in similarity_scores if artist_final.iloc[i]['artists'].lower() != query_artist.lower()]
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    top_matches = similarity_scores[:top_n]

    artists = [artist_final.iloc[i]['artists'] for i, _ in top_matches]
    scores = [score for _, score in top_matches]

    # Use actual scores to color match darker = higher similarity
    norm_scores = [(s - min(scores)) / (max(scores) - min(scores)) if max(scores) > min(scores) else 0.5 for s in scores]
    color_map = sns.color_palette("mako", as_cmap=True)
    bar_colors = [color_map(s) for s in norm_scores]

    # Bar graph visualization (corrected shading and length behavior)
    plt.figure(figsize=(10, 6))
    bars = plt.barh(artists, scores, color=bar_colors, edgecolor='black')
    plt.xlabel("Similarity Score")
    plt.ylabel("Similar Artists")
    plt.title(f"Top {top_n} Artists Similar to {query_artist}")
    plt.xlim(0, 1.05)
    plt.gca().invert_yaxis()

    # Add score labels to bars
    for bar, score in zip(bars, scores):
        plt.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height() / 2,
                 f"{score:.3f}", va='center', ha='left', fontsize=9)

    plt.tight_layout()
    plt.savefig(f"{query_artist.replace(' ', '_')}_similarity_barplot.png", dpi=300)
    plt.show()

    # Tabular display in console
    results_df = pd.DataFrame({'Artist': artists, 'Similarity Score': [round(s, 3) for s in scores]})
    print("\nTop Similar Artists:")
    print(results_df.to_string(index=False))

    return results_df

# --- Step 6: Interactive Prompt ---
query_input = input("Insert artist name: ")
results_df = get_top_matches(query_input)

if results_df is not None:
    results_df.to_csv(f"{query_input.replace(' ', '_')}_top_similar.csv", index=False)
