# Loading in required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

nobel = pd.read_csv('nobel.csv')

# What is the most commonly awarded gender and birth country?
top_gender = nobel['sex'].value_counts().index[0]
top_country = nobel['birth_country'].value_counts().index[0]

# Which decade and Nobel Prize category combination had the highest proportion of female laureates?
nobel["us_winners"] = nobel["birth_country"] == "United States of America"
nobel["decade"] = (np.floor(nobel['year']/10) * 10).astype(int)
prop_us_winners = nobel.groupby("decade", as_index=False)["us_winners"].mean()

# setting as_index=False, you make sure the result is saved as a DataFrame rather than a series
print(prop_us_winners)

max_decade_usa = prop_us_winners[prop_us_winners["us_winners"] == prop_us_winners["us_winners"].max()]['decade'].values[0]
print(max_decade_usa)