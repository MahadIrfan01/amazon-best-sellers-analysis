Bestsellers Data Analysis (Pandas)

This project performs exploratory data analysis and cleaning on a bestselling books dataset using Python and Pandas. It cleans raw data, generates summary statistics, extracts insights about authors, genres, pricing, and ratings, and exports analysis-ready CSV files.

**🔧 Features**

Cleans and standardizes raw dataset

Removes duplicate entries

Renames columns for consistency

Converts price data to numeric format

Performs author and genre-based analysis

Analyzes trends over publication years

Computes correlation between book price and user ratings

Exports multiple CSV files for further analysis or visualization

**📁 Input**

The script expects a CSV file named:

bestsellers.csv

Required Columns

Name

Author

Genre

Rating

Price

Publication Year

If any required column is missing, the program will raise an error.

**📤 Output Files**

The script generates the following files:

File Name	Description
cleaned_bestsellers.csv	Fully cleaned dataset
top_authors.csv	Top 10 authors by number of books
avg_rating.csv	Average user rating by genre
top_books.csv	Top 10 highest-rated books
avg_price_by_genre.csv	Average book price per genre
books_per_year.csv	Number of books published per year
rating_trend.csv	Average rating over time
🚀 How to Run

Install dependencies:

pip install pandas


Place bestsellers.csv in the project directory

Run the script:

python analysis.py

**📊 Example Insights**

Identifies most prolific authors

Compares genre popularity and quality

Tracks how ratings change over time

Evaluates whether higher-priced books receive better ratings

**🧠 Tech Stack**

Python 3

Pandas

📌 Notes

Designed to fail fast if the dataset is malformed

All outputs are CSV files for easy reuse in dashboards or reports

Easily extendable with visualizations or machine learning models
