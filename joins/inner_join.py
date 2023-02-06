# INNER JOIN with Pandas
# (source: https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html#join)
import pandas as pd

# Addressing the data file paths
dataset1 = ("../data/My favorite actors and actresses.csv")
dataset2 = ("../data/Most movies.csv")

# Importing the datasets (.csv files)
my_fav_actors_and_actresses = pd.read_csv(dataset1)
most_movies = pd.read_csv(dataset2)

# JOINs can be performed with join() or merge(). By default,
# join() will join the DataFrames on their indices.
# Each method has parameters allowing you to specify the type
# of join to perform (LEFT, RIGHT, INNER, FULL) or the columns
# to join on (column names or indices).

# Merging both tables using the column 'Name' as key using INNER JOIN
# In SQL that would be:
# SELECT *
# FROM my_fav_actors_and_actresses
#   INNER JOIN most_movies
#       ON my_fav_actors_and_actresses.Name = most_movies.Name;
inner_join_tables = pd.merge(my_fav_actors_and_actresses, most_movies, on="Name")
print(inner_join_tables)

# merge() also offers parameters for cases when you’d like
# to join one DataFrame’s column with another DataFrame’s index.
indexed_most_movies = most_movies.set_index("Name")
inner_join_tables_one = pd.merge(my_fav_actors_and_actresses,
                                 indexed_most_movies, left_on="Name", right_index=True)
print(inner_join_tables_one)