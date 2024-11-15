# Loading in required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

nobel = pd.read_csv('nobel.csv')

# What is the most commonly awarded gender and birth country?
top_gender = nobel['sex'].value_counts().index[0]
top_country = nobel['birth_country'].value_counts().index[0]

# Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?
nobel["us_winners"] = nobel["birth_country"] == "United States of America"
nobel["decade"] = (np.floor(nobel['year']/10) * 10).astype(int)
prop_us_winners = nobel.groupby("decade", as_index=False)["us_winners"].mean()

# setting as_index=False, you make sure the result is saved as a DataFrame rather than a series
print(prop_us_winners)

max_decade_usa = prop_us_winners[prop_us_winners["us_winners"] == prop_us_winners["us_winners"].max()]['decade'].values[0]
print(max_decade_usa)

# Which decade and Nobel Prize category combination had the highest proportion of female laureates?
nobel['female_winner'] = nobel['sex'] == 'Female'
# Group by decade and prize category, then calculate the mean of female laureates
prop_female_winner = nobel.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()
# Find the decade and category with the highest proportion of female laureates
max_female_decade_category = prop_female_winner[prop_female_winner['female_winner'] == prop_female_winner['female_winner'].max()][['decade', 'category']]
max_female_dict = {
    max_female_decade_category['decade'].values[0]:max_female_decade_category['category'].values[0]
}
print(max_female_dict)

# Finding the first woman to win a Nobel Prize
nobel_women = nobel[nobel['female_winner']]
min_row = nobel_women[nobel_women['year'] == nobel_women['year'].min()]
first_woman_name = min_row['full_name'].values[0]
first_woman_category = min_row['category'].values[0]
print(f"\n The first woman to win a Nobel Prize was {first_woman_name}, in the category of {first_woman_category}.")

# Selecting the laureates that have received 2 or more prizes
counts = nobel['full_name'].value_counts()
repeats = counts[counts >= 2].index
repeat_list = list(repeats)

print("\n The repeat winners are :", repeat_list)