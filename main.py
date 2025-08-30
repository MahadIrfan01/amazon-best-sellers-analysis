import pandas as pd
df = pd.read_csv('bestsellers.csv')



df.drop_duplicates(inplace=True)
df.rename(columns={
    "Name":"Title",
    "Publication Year": "Publication year",
    "Rating": "User Rating"
}, inplace=True)

df["Price"] = df["Price"].astype(float)

print(df.head())
print(df.shape)
print(df.describe())
print(df.columns)

author_counts = df['Author'].value_counts()
avg_rating = df.groupby("Genre")["User Rating"].mean()
print(author_counts)
print(avg_rating)

author_counts.head(10).to_csv("top_authors.csv")
avg_rating.to_csv("avg_rating.csv")

