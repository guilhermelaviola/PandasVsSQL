# Using LIMIT with Pandas
# (source: https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html#limit)
import pandas as pd

# Addressing the data file paths
dataset = ("../data/My favorite actors and actresses.csv")

# Importing the datasets (.csv files)
my_fav_actors_and_actresses = pd.read_csv(dataset)

# Limiting the query result to 10 rows
# In SQL that would be:
# SELECT *
# FROM my_fav_actors_and_actresses
# LIMIT 10;
select_with_limit = my_fav_actors_and_actresses.head(10)
print(select_with_limit)