import pandas as pd
import random

#Loading CSV in Pandas DataFrame
my_csv = pd.read_csv('Dates 10f26e397f9c4b6da70d310139e5cd02.csv')
activityNames = my_csv.Name

#Selects random item from list
print(random.choice(activityNames))