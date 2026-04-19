
import pandas as pd
data = pd.read_csv('laborator_4_exercitii/data.csv')    
filtered_data = data[data['Age'] > 40]
print(filtered_data.head(10))
