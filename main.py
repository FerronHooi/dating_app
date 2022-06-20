import pandas as pd

#Loading CSV in Pandas DataFrame
my_csv = pd.read_csv('Dates 10f26e397f9c4b6da70d310139e5cd02.csv')
activityNames = my_csv.Name

for activity in activityNames:
    print(activity)