
import pandas as pd
data = pd.read_csv('laborator_4_exercitii/data.csv')
filtered_data = data[(data['Overall'] >= 85) & (data['Age'] < 25)]
print(filtered_data)