#Aflați care club are cea mai mare medie de Overall.
import pandas as pd
data = pd.read_csv('laborator_4_exercitii/data.csv')
grouped_data = data.groupby('Club')['Overall'].mean()
max_overall_club = grouped_data.idxmax()
print(f"Clubul cu cea mai mare medie de Overall este: {max_overall_club}")
                                                       