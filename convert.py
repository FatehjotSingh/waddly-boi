import csv
import pandas as pd

data = []

file = pd.read_csv('dwarf_stars.csv')

file = file.dropna()

file['Radius'] = 0.102763* file['Radius']
file['Mass'] = file['Mass'].apply(lambda x : x.replace('$','').replace(',','')).astype('float')

file['Mass'] = 0.000954588 * file['Mass']

file.drop(['Unnamed'], axis =1, inplace = True)
file.reset_index(drop = True, inplace = True)

file.to_csv('stars.csv')