#! /usr/bin/python

import pandas as pd

# Read the csv
table_bsa = pd.read_csv('Data/Cells_on_BSA_Experiments.csv')
table_slb = pd.read_csv('Data/Cells_Experiments.csv')

# Drop columns
table_bsa = table_bsa.drop(['Date', 'Undefined_Ad', 'Small_Bl', 'Big_Bl', 'Enormous_Bl', 'Notes'], axis=1)
table_slb = table_slb.drop(['Date'], axis=1)

# Rename columns
table_bsa = table_bsa.rename(columns={'No_Ad':'No', 'Small_Ad':'Small', 'Big_Ad':'Big'})
table_slb = table_slb.rename(columns={'No_Ad':'No', 'Small_Ad':'Small', 'Big_Ad':'Big'})

# Adhesion ratio
table_bsa['Rbig'  ] = table_bsa['Big']   / (table_bsa['No'] + table_bsa['Small'])
table_slb['Rsmall'] = table_slb['Small'] /  table_slb['No']

# print the tables in latex format
print(table_bsa.round(2).to_latex(index=False))
print(table_slb.round(2).to_latex(index=False))