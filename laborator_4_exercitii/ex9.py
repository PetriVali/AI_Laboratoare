#Calculați media atributelor ‘SprintSpeed’ și ‘Acceleration’ pentru fiecare naționalitate. (groupby("Nationality"))
import pandas as pd
data = pd.read_csv('laborator_4_exercitii/data.csv')
grouped_data = data.groupby('Nationality')[['Sprint Speed', 'Acceleration']].mean()
print(grouped_data)
