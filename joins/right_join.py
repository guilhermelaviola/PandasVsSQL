# RIGHT JOIN with Pandas
# (source: https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html#join)
import pandas as pd

# Addressing the data file paths
dataset1 = ("../data/My favorite actors and actresses.csv")
dataset2 = ("../data/Most movies.csv")

# Importing the datasets (.csv files)
my_fav_actors_and_actresses = pd.read_csv(dataset1)
most_movies = pd.read_csv(dataset2)

# Merging both tables using the column 'Name' as key using RIGHT JOIN
# In SQL that would be:
# SELECT *
# FROM my_fav_actors_and_actresses
#   RIGHT JOIN most_movies
#       ON my_fav_actors_and_actresses.Name = most_movies.Name;
right_join_tables = pd.merge(my_fav_actors_and_actresses, most_movies, on="Name", how="right")
print(right_join_tables)