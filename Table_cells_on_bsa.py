#! /usr/bin/python

# Libraries
import pandas as pd
import os 

# Extract the name of each experiment directory
Experiments = os.listdir('Data/Cells_on_BSA/')
# Sort the experiment list
Experiments.sort()

# Extract the date, discription, incubation, adhesion and notes
Date, Discription, Incubation, Adhesion, Notes = [], [], [], [], []
for experiment in Experiments:
    # Extract the date
    Date.append(experiment.split('_')[0])
    # Extract the discription
    discription = ''
    for word in experiment.split('_')[1:]:
        discription += word + ' '
    Discription.append(discription)
    # Extract the incubations, adhesion and notes from each directory
    Chambers = os.listdir(f'Data/Cells_on_BSA/{experiment}')
    Chambers_list = []
    for Chamber in Chambers:
        Chambers_list.append(Chamber.replace('_', ' '))
        Adhesion.append(open(f'Data/Cells_on_BSA/{experiment}/{Chamber}/table.csv').readlines()[1][:-1])
        Notes.append(open(f'Data/Cells_on_BSA/{experiment}/{Chamber}/note.txt').read()[:-1])        
    Incubation.append(Chambers_list)

# Assign the data.  
data = {'Date':Date, 'Discription':Discription, 'Incubation':Incubation}
  
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
df['Adhesion'] = Adhesion
df[['No', 'Small', 'Big', 'Undefined']] = df['Adhesion'].str.split(',',expand=True)
df = df.drop(['Adhesion'], axis=1)


# Assign the notes
df['Notes']= Notes

# Save the DataFrame.  
df.to_csv('Data/Cells_on_BSA_Experiments.csv', index=False)

# Print the DataFrame
print(df)