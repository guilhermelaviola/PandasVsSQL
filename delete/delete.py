# DELETE with Pandas
import pandas as pd

dataset = ("../data/football-transfers.csv")

# Importing the dataset (.csv file)
summer_transfers = pd.read_csv(dataset)

# Deleting players with ages under 17 and displaying the result
# In SQL that would be:
# DELETE age
# from summer_transfers
# WHERE age > 17;
# In pandas we select the rows that should remain instead of deleting them
summer_transfers.loc[summer_transfers["age"] <= 17]
updated_young_age_after_deletion = summer_transfers[summer_transfers["age"] < 17]
print(updated_young_age_after_deletion)