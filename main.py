import pandas as pd
import random

Tijdsduur = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)

# TODO: Show count of each individual activityS/D/N
#Loading CSV in Pandas DataFrame
my_csv = pd.read_csv('Dates 10f26e397f9c4b6da70d310139e5cd02.csv')

# TODO: Get only distinct value from lists beneath

#function below removes nan from list and shows only unique values in the list
def activityProperty(csv_column):
    activityProperty = csv_column.tolist()
    activityProperty = list(set([item for item in activityProperty if not (pd.isnull(item)) == True]))
    print(activityProperty)

activityLocation = activityProperty(my_csv.Locatie)
activityNames = activityProperty(my_csv.Name)
activityStatus = activityProperty(my_csv.Status)
activityDurage = activityProperty(my_csv.Duur)




# TODO: Fix inquirer
#use inquirer to let user select from list
"""questions = [
  inquirer.List('size',
                message="What is the durage you want to get a random activity from?",
                choices=activityDurage,
            ),
]
answers = inquirer.prompt(questions)
print (answers["size"])"""

# TODO: If user executes this scripts then
    # 1. He should pick a status (or not)
    # 2. He should then pick a max duration (or not)
    # 3. He should be asked to pick a location (or not)


#Selects random item from list
print(random.choice(activityNames))