# Loading in required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

nobel = pd.read_csv('nobel.csv')

# What is the most commonly awarded gender and birth country?
top_gender = nobel['sex'].value_counts().index[0]