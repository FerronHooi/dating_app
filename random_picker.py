import pandas as pd
import random
from main import activityProperty

#Loading CSV in Pandas DataFrame
my_csv = pd.read_csv('Dates 10f26e397f9c4b6da70d310139e5cd02.csv')

activityLocation = activityProperty(my_csv.Locatie)
activityNames = activityProperty(my_csv.Name)
activityStatus = activityProperty(my_csv.Status)
activityDurage = activityProperty(my_csv.Duur)

# TODO: If the status 'Films & TV' is selected then "watch" will appear in front of it
print("You and your date will do the following, have fun! :)")
print(random.choice(list(activityNames)))

# TODO: IDEA: A random activity/durage and location will be picked for the user when clicking this button!. Status should be removed from this
#Selects random item from list
print("You and your date will do the following, have fun! :)")
print("The location will be:", random.choice(list(activityLocation)))
print("The activity will be:", random.choice(list(activityNames)))
print("The durage will be:", random.choice(list(activityDurage)))