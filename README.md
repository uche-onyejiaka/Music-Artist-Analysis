<<<<<<< HEAD
# 🎧 Music Similarity Analysis  
**INST 414: Data Science Techniques**  
Created by Uche K.

🔗 [View on GitHub](https://github.com/uche-onyejiaka/Music-Artist-Analysis)

---

## 🧠 What This Project Does

This project uses data science to answer one simple but powerful question:

> **“Who sounds most like [insert artist here]?”**

By analyzing audio features and genre information from the Spotify Million Song Dataset, this tool helps identify the top 10 artists who sound the most similar to a user-specified artist — with visual and tabular results.

---

## 📁 Dataset Overview

This project is built using a cleaned subset of the [Spotify Million Song Dataset](https://www.kaggle.com/datasets/zaheenhamidani/spotify-million-song-dataset). Key features used:
- `artists`
- `track_genre`
- `popularity`
- `danceability`
- `energy`
- `valence`
- `speechiness`
- `acousticness`

---

## 🧮 How It Works 

1. Each artist is turned into a vector using audio features and genre encodings.
2. Cosine similarity is used to compare all artists and rank their similarity.
3. The system returns the top 10 most similar artists for any query.

Why cosine similarity? It focuses on the **direction** of each artist’s musical profile — making it ideal for comparing style rather than raw volume or popularity.


---

## 📊 What You'll see

When you run the script, you'll:

When you run the code:
- You’ll be prompted to input an artist (e.g., `Beyoncé`)
- You’ll get a clean **horizontal bar chart** where:
  - Bar length = similarity score
  - Bar color = similarity strength (darker = more similar)
- A similarity score label is displayed on each bar
- You’ll also see a printed **table** in the terminal

Both the graph and the table are saved automatically as:
- `artistname_similarity_barplot.png`
- `artistname_top_similar.csv`

---

## ▶️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/uche-onyejiaka/Music-Artist-Analysis.git
cd Music-Artist-Analysis

2. Make sure you have Python 3 and the following libraries installed:

pip install pandas numpy scikit-learn matplotlib seaborn

3. Run the script:

python Artist_Similarity_Analysis.py

4. When prompted:

Insert artist name: Beyoncé  (example)

5. Results

Upon hitting enter you will see a graph with the visualization and results


📬 Questions or Feedback?

Feel free to fork, remix, or reach out.

This was built as part of my INST 414 course at the University of Maryland — but it's something I could easily see becoming a personal playlist tool or even a plug-in for recommendation engines.

=======
# Music-Artist-Analysis
>>>>>>> 04170b9e4028c2c900d9c813e3324ffb26932286
