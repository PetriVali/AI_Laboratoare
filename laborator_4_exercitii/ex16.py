import pandas as pd
from bokeh.plotting import figure, show

data = pd.read_csv('laborator_4_exercitii/data.csv')

for col in ['Wage', 'Value']:
    data[col] = pd.to_numeric(data[col].replace(r'[€K M]|', '', regex=True), errors='coerce').fillna(0)

p = figure(tooltips=[("Nume", "@Name"), ("Salariu", "@Wage"), ("Valoare", "@Value")])
p.circle('Wage', 'Value', source=data, size=10)

show(p)