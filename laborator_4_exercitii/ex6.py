
import pandas as pd
data = pd.read_csv('laborator_4_exercitii/data.csv')
num_rows, num_cols = data.shape
num_unique_players = data['Name'].nunique()
print(f"Număr de rânduri: {num_rows}")
print(f"Număr de coloane: {num_cols}")
print(f"Număr de jucatori unici: {num_unique_players}")
print(f"Număr de coloane: {num_cols}")