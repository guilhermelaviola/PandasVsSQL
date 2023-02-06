# UNION with Pandas
# (source: https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html#union)
import pandas as pd

# Addressing the data file paths
dataset1 = ("../data/My favorite actors and actresses.csv")
dataset2 = ("../data/Most movies.csv")

# Importing the datasets (.csv files)
my_fav_actors_and_actresses = pd.read_csv(dataset1)
most_movies = pd.read_csv(dataset2)

# Concatenating both tables with UNION ALL (with duplicate rows)
# In SQL that would be:
# SELECT *
# FROM my_fav_actors_and_actresses
# UNION ALL
# SELECT *
# FROM most_movies;
union_all_tables = pd.concat([my_fav_actors_and_actresses, most_movies])
print(union_all_tables)

# Concatenating both tables with UNION ALL (without duplicate rows)
# In SQL that would be:
# SELECT *
# FROM my_fav_actors_and_actresses
# UNION
# SELECT *
# FROM most_movies;
union_all_tables_without_duplicates = pd.concat([my_fav_actors_and_actresses, most_movies]).drop_duplicates()
print(union_all_tables_without_duplicates)