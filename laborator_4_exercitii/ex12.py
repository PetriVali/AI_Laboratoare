#Câți jucători au o valoare de transfer mai mare decât salariul?
import pandas as pd
data = pd.read_csv('laborator_4_exercitii/data.csv')
filtered_data = data[data['Value'] > data['Wage']]
num_players = filtered_data.shape[0]
print(f"Numărul de jucători cu valoare de transfer mai mare decât salariul este: {num_players}")
