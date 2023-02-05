import numpy as np
import pandas as pd

dataset = ("../data/football-transfers.csv")

# Importing the dataset (.csv file)
summer_transfers = pd.read_csv(dataset)

# Selecting all columns and grouping players by position
# In SQL that would be:
# SELECT position, COUNT(*)
# FROM summer_transfers
# GROUP BY position;
group_by_position = summer_transfers.groupby("position").size()
print(group_by_position)

# Notice that in the pandas code we used size() and not count().
# This is because count() applies the function to each column,
# returning the number of NOT NULL records within each.
# Alternatively, we could have applied the count() method to an individual column:
origin_club_grouped_by_position = summer_transfers.groupby("position")["origin_club"].count()
print(origin_club_grouped_by_position)

# Selecting the position column and returning extra columns with the average age by
# and the amount of players by position
# In SQL that would be:
# SELECT position, AVG(age), COUNT(*)
# FROM summer_transfers
# GROUP BY position;
group_by_position_with_age_mean = summer_transfers.groupby("position").agg({"age": np.mean, "position": np.size})
print(group_by_position_with_age_mean)

# Selecting the columns position ans age and returning extra columns with the average age by
# and the amount of players by position grouped by position and age
# In SQL that would be:
# SELECT position, age, COUNT(*), AVG(age)
# FROM summer_transfers
# GROUP BY position, age;
group_by_position_and_age_with_age_mean = summer_transfers.groupby(["position", "age"]).agg({"age": [np.size, np.mean]})
print(group_by_position_and_age_with_age_mean)