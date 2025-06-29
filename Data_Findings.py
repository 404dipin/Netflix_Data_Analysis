#Importing libraries and loading data
#libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#read the netflix data
df=pd.read_csv('netflix_titles.csv',encoding='latin1')
print(df)

#basic exploration
print("shape of the datasets",df.shape)
print("\n columns:\n",df.columns)
print("\n Dataset info")
print(df.info())

print("\n Missing Values:\n")
print(df.isnull().sum())

#Data cleaning
df['country']=df['country'].fillna('unknown')
df['rating']=df['rating'].fillna('unknown')
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df['year_added'] = df['date_added'].dt.year
df.to_csv('netflix_cleaned.csv')

#types of content (movie vs tv.shows)
type_counts = df['type'].value_counts()

# Bar plot
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color='skyblue')
plt.title("Count of Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig('Movies_vs_tvshows.png',dpi=300,bbox_inches='tight')
plt.show()

#content added by year
year_counts = df['year_added'].value_counts().sort_index()

plt.figure(figsize=(10,5))
plt.plot(year_counts.index, year_counts.values, marker='o', linestyle='-', color='orange')
plt.title("Number of Shows Added Each Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.grid(True, linestyle="--", alpha=0.5)
plt.xticks(rotation=45)
plt.savefig('No_of_shows_added_each_year.jpg',dpi=300,bbox_inches='tight')
plt.show()

#top 10 countries with most content
country_counts = df['country'].value_counts().head(10)

plt.figure(figsize=(8,5))
plt.barh(country_counts.index, country_counts.values, color='green')
plt.title("Top 10 Countries by Content")
plt.xlabel("Count")
plt.ylabel("Country")
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig('Top_10_contry_by_content.jpg',dpi=300,bbox_inches='tight')
plt.show()

#top 10 most common genres
# Many genres are comma-separated; split and count them
genre_series = df['listed_in'].dropna().str.split(', ')
all_genres = [genre for sublist in genre_series for genre in sublist]
genre_counts = pd.Series(all_genres).value_counts().head(10)

plt.figure(figsize=(8,5))
plt.barh(genre_counts.index[::-1], genre_counts.values[::-1], color='purple')
plt.title("Top 10 Most Common Genres")
plt.xlabel("Number of Titles")
plt.grid(True, axis='x', linestyle="--", alpha=0.5)
plt.savefig('Common_genres.jpg',dpi=300,bbox_inches='tight')
plt.show()
