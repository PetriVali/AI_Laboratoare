
import pandas as pd
data = pd.read_csv('laborator_4_exercitii/data.csv')
data['Custom Score'] = (0.3 * data['Overall'] +0.3 * data['Potential'] + 0.2 * data['SprintSpeed'] + 0.2 * data['ShortPassing'])
print(data[['Name', 'Custom Score']])   