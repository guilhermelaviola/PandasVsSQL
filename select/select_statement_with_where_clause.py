# Performing basic SQL SELECT with WHERE clause with Pandas
import pandas as pd

dataset = ("../data/football-transfers.csv")

# Importing the dataset (.csv file)
summer_transfers = pd.read_csv(dataset)

# Selecting all columns where the origin league is Serie A (from Italy)
# In SQL that would be:
# SELECT *
# FROM summer_transfers
# WHERE league_origin_club = 'Serie A';
transfers_from_serie_a = summer_transfers[summer_transfers["league_origin_club"] == "Serie A"]
print(transfers_from_serie_a)

# Selecting all columns where players age are under or equal 18
# In SQL that would be:
# SELECT *
# FROM summer_transfers
# WHERE age <= 18;
young_players = summer_transfers[summer_transfers["age"] <= 18]
print(young_players)

# Returning the amount of players with age equal or under 18
# In SQL that would be:
# SELECT COUNT(*)
# FROM summer_transfers
# WHERE age <= 18;
is_player_under_18 = summer_transfers["age"] <= 18
print(is_player_under_18.value_counts())

# Returning the amount of goalkeepers with age equal or under 18
# In SQL that would be:
# SELECT COUNT(*)
# FROM summer_transfers
# WHERE age <= 18 AND position == 'Goalkeeper';
is_player_under_18_and_goalkeeper = (summer_transfers["age"] <= 18) & (summer_transfers["position"] == "Goalkeeper")
print(is_player_under_18_and_goalkeeper.value_counts())

# Returning players who are over 30 years old or who are defensive midfielders
# In SQL that would be:
# SELECT *
# FROM summer_transfers
# WHERE age == 30 OR position == 'Defensive Midfield';
players_over_30_or_defensive_midfielders = summer_transfers[(summer_transfers["age"] == 30) | (summer_transfers["position"] == "Defensive Midfield")]
print(players_over_30_or_defensive_midfielders)

# Checking if there are any null rows in age column and returning the amount
# In SQL that would be:
# SELECT *
# FROM summer_transfers
# WHERE age IS NULL;
age_null = summer_transfers["age"].isna()
print(age_null.value_counts())

# Checking if there are any not null rows in age column and returning the amount
# In SQL that would be:
# SELECT *
# FROM summer_transfers
# WHERE age IS NOT NULL;
age_not_null = summer_transfers["age"].notna()
print(age_not_null.value_counts())