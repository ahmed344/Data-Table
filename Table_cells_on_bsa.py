#! /usr/bin/python

# Libraries
import numpy as np
import pandas as pd
import os 

# Extract the name of each experiment directory
experiments = os.listdir('Data/Cells_on_BSA/')
# Sort the experiment list
experiments.sort()

# Extract the date, discription, incubation, adhesion and notes
date, discriptions, incubation, adhesions, blebs, notes = [], [], [], [], [], []
for experiment in experiments:
    # Extract the date
    date.append(experiment.split('_')[0])
    # Extract the discription
    discription = ''
    for word in experiment.split('_')[1:]:
        discription += word + ' '
    discriptions.append(discription)
    # Extract the incubations, adhesion and notes from each directory
    chambers = os.listdir(f'Data/Cells_on_BSA/{experiment}')
    chambers_list = []
    for chamber in chambers:
        chambers_list.append(chamber.replace('_', ' '))
        adhesions.append(open(f'Data/Cells_on_BSA/{experiment}/{chamber}/table.csv').readlines()[1][:-1])
        blebs.append(open(f'Data/Cells_on_BSA/{experiment}/{chamber}/table.csv').readlines()[3][:-1])
        notes.append(open(f'Data/Cells_on_BSA/{experiment}/{chamber}/note.txt').read()[:-1])        
    incubation.append(chambers_list)

# Assign the data.  
data = {'Date':date, 'Discription':discriptions, 'Incubation':incubation}
  
# Create the DataFrame  
df = pd.DataFrame(data) 

# Explode the Incubation column
df = df.explode('Incubation') 

# Split the Incubation column into Incubation and Observation
df[['Incubation', 'Observation']] = df['Incubation'].str.split('=',expand=True)

# Replace positive and negative by with Ecad and without Ecad
df['Incubation'] = df['Incubation'].str.replace('positive', 'with Ecad')
df['Incubation'] = df['Incubation'].str.replace('negative', 'without Ecad')

# Assign the adhesion
df['Adhesion'] = adhesions
df[['No_Ad', 'Small_Ad', 'Big_Ad', 'Undefined_Ad']] = df['Adhesion'].str.split(',',expand=True)
df = df.drop(['Adhesion'], axis=1)

# Assign the blebs
df['Blebs'] = blebs
df[['Small_Bl', 'Big_Bl', 'Enormous_Bl']] = df['Blebs'].str.split(',',expand=True)
df = df.drop(['Blebs'], axis=1)


# Assign the notes
df['Notes']= notes

# Save the DataFrame.  
df.to_csv('Data/Cells_on_BSA_Experiments.csv', index=False)

# Print the DataFrame
print(df)