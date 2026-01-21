import pandas as pd

# Load data
df = pd.read_csv("bestsellers.csv")

# ----------------------------
# Basic cleaning
# ----------------------------
df.drop_duplicates(inplace=True)

df.rename(columns={
    "Name": "Title",
    "Publication Year": "Publication year",
    "Rating": "User Rating"
}, inplace=True)

df["Price"] = df["Price"].astype(float)

# ----------------------------
# Sanity checks (non-breaking)
# ----------------------------
required_columns = ["Title", "Author", "Genre", "User Rating", "Price", "Publication year"]
missing = [col for col in required_columns if col not in df.columns]
if missing:
    raise ValueError(f"Missing required columns: {missing}")

# ----------------------------
# Core outputs (your original logic)
# ----------------------------
print(df.head())
print(df.shape)
print(df.describe())
print(df.columns)

author_counts = df["Author"].value_counts()
avg_rating = df.groupby("Genre")["User Rating"].mean()

print(author_counts)
print(avg_rating)

author_counts.head(10).to_csv("top_authors.csv")
avg_rating.to_csv("avg_rating.csv")

# ----------------------------
# Added features
# ----------------------------

# 1. Top 10 highest-rated books
top_books = df.sort_values(by="User Rating", ascending=False).head(10)
top_books.to_csv("top_books.csv", index=False)

# 2. Average price by genre
avg_price_by_genre = df.groupby("Genre")["Price"].mean()
avg_price_by_genre.to_csv("avg_price_by_genre.csv")

# 3. Books published per year
books_per_year = df["Publication year"].value_counts().sort_index()
books_per_year.to_csv("books_per_year.csv")

# 4. Rating trend over time
rating_trend = df.groupby("Publication year")["User Rating"].mean()
rating_trend.to_csv("rating_trend.csv")

# 5. Correlation between price and rating
price_rating_corr = df["Price"].corr(df["User Rating"])
print(f"Correlation between price and user rating: {price_rating_corr:.3f}")

# 6. Save cleaned dataset
df.to_csv("cleaned_bestsellers.csv", index=False)
