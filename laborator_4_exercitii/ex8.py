#Reprezentați într-un pie chart proporția jucătorilor pe naționalități (top 5).
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('laborator_4_exercitii/data.csv')
nationality_counts = data['Nationality'].value_counts().head(5)
plt.figure(figsize=(8, 8))  
plt.pie(nationality_counts, labels=nationality_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Proporția jucătorilor pe naționalități (top 5)')
plt.axis('equal')
plt.show()
