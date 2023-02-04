# Performing basic SQL SELECT with Pandas
import pandas as pd

dataset = ("../data/football-transfers.csv")

# Importing the dataset (.csv file)
summer_transfers = pd.read_csv(dataset)

# Selecting all columns and rows from summer_transfers
# In SQL that would be:
# SELECT *
# FROM summer_transfers;
all_columns = summer_transfers.head(10)
print(all_columns)

# Selecting columns name, former club and new club from summer_transfers
# In SQL that would be:
# SELECT name, origin_club, new_club
# FROM summer_transfers;
some_columns = summer_transfers[["name", "origin_club", "new_club"]]
print(some_columns)

# Selecting all columns and creating a resulting column based on age data
# In SQL that would be:
# SELECT * age+1 AS age_in_one_year
# FROM summer_transfers;
new_age = summer_transfers.assign(age_in_one_year=summer_transfers["age"] + 1)
print(new_age)