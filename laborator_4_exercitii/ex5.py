#Filtrați jucătorii care au contractul până în 2021.
import pandas as pd
data = pd.read_csv('laborator_4_exercitii/data.csv')
filtered_data = data[data['Contract Valid Until'] == 2021]
print(filtered_data)
