import pandas as pd
import random
import inquirer


#Loading CSV in Pandas DataFrame
my_csv = pd.read_csv('Dates 10f26e397f9c4b6da70d310139e5cd02.csv')
activityNames = my_csv.Name
activityStatus = my_csv.Status
activityDurage = my_csv.Duur\
    .tolist()
activityLocation = my_csv.Locatie.tolist()
Tijdsduur = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)

#use inquirer to let user select from list
"""questions = [
  inquirer.List('size',
                message="What is the durage you want to get a random activity from?",
                choices=activityDurage,
            ),
]
answers = inquirer.prompt(questions)
print (answers["size"])"""


#Selects random item from list
print(random.choice(activityNames))