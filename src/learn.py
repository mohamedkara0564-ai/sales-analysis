from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from cleaning import load_and_clean_data
import pandas as pd

data = load_and_clean_data()
# print(data[0].head())

a, b = load_and_clean_data()
print(a.head(10))
