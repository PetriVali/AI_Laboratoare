#Completați valorile lipsă din coloana 'Position' cu stringul "Unknown".
import pandas as pd
data = pd.read_csv('laborator_4_exercitii/data.csv')
data['Position'] = data['Position'].fillna('Unknown')
print(data['Position'])
