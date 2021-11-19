#! /usr/bin/python

# Libraries
import pandas as pd
import os 

# Extract the name of each experiment directory
Experiments = os.listdir('Data/Cells/')
# Sort the experiment list
Experiments.sort()

# Extract the date, discription and incubation
Date, Discription, Incubation = [], [], []
for experiment in Experiments:
    # Extract the date
    Date.append(experiment.split('_')[0])
    # Extract the discription
    discription = ''
    for word in experiment.split('_')[1:]:
        discription += word + ' '
    Discription.append(discription)
    # Extract the incubations from each directory
    Chambers = os.listdir('Data/Cells/{}'.format(experiment))
    Chambers_list = []
    for Chamber in Chambers:
        Chambers_list.append(Chamber.replace('_', ' '))
    Incubation.append(Chambers_list)

# Assign the data.  
data = {'Date':Date, 'Discription':Discription, 'Incubation':Incubation}
  
# Create the DataFrame  
df = pd.DataFrame(data) 

# Explode the Incubation column
df = df.explode('Incubation') 

# Split the Incubation column into Incubation and Observation
df[['Incubation','Observation']] = df['Incubation'].str.split('=',expand=True)

# Save the DataFrame.  
df.to_csv('Data/Cells_Experiments.csv', index=False)

# Print the DataFrame
print(df)