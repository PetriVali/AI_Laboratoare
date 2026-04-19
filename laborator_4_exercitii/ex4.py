#Sortează jucătorii după Skill Moves descrescător.
import pandas as pd
data = pd.read_csv('laborator_4_exercitii/data.csv')
sorted_data = data.sort_values(by='Skill Moves', ascending=False)
print(sorted_data)