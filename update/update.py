# UPDATE with Pandas
import pandas as pd

dataset = ("../data/football-transfers.csv")

# Importing the dataset (.csv file)
summer_transfers = pd.read_csv(dataset)

# Updating ages under 17 by adding +2 to them and displaying the result
# In SQL that would be:
# UPDATE age
# SET age = age + 2
# WHERE age < 17;
summer_transfers.loc[summer_transfers["age"] < 17, "age"] + 2
updated_young_age = summer_transfers[summer_transfers["age"] < 17]
print(updated_young_age)