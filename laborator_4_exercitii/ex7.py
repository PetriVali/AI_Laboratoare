#Care este cea mai frecventa nationalitate a jucatorilor? Afisati top 5 nationalitati.
import pandas as pd
data = pd.read_csv('laborator_4_exercitii/data.csv')
nationality_counts = data['Nationality'].value_counts()
print(nationality_counts.head(5))