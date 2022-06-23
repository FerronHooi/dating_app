import pandas as pd
import random
from collections import Counter

# TODO: Also add column which user added which activity --> in order to also be able to select based on who

# TODO: User should be able to enter a max tijdsduur
Tijdsduur = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)

#Loading CSV in Pandas DataFrame
my_csv = pd.read_csv('Dates 10f26e397f9c4b6da70d310139e5cd02.csv')

#function below removes nan from list and shows only unique values in the list and orders it in alphabetical order
def activityProperty(csv_column):
    activityProperty = csv_column.tolist()
    activityProperty = sorted(list(set([item for item in activityProperty if not (pd.isnull(item)) == True])))
    #print(activityProperty)
    return(activityProperty)

#fumction below shows the count of each occurence
def activityPropertyCount(csv_column):
    activityProperty = csv_column.tolist()
    activityCount = Counter(sorted(list([item for item in activityProperty if not (pd.isnull(item)) == True])))
    #print(activityCount)
    return(activityCount)

activityLocation = activityProperty(my_csv.Locatie)
activityLocationCount = activityPropertyCount(my_csv.Locatie)

activityNames = activityProperty(my_csv.Name)
activityNamesCount = activityPropertyCount(my_csv.Name)

activityStatus = activityProperty(my_csv.Status)
activityStatusCount = activityPropertyCount(my_csv.Status)

activityDurage = activityProperty(my_csv.Duur)
activityDurageCount = activityPropertyCount(my_csv.Duur)

# TODO: If user picks a number only options should be shown that can be picked based on previous chosen option


def let_user_pick(options):
    print("Please choose:")

    for idx, element in enumerate(options):
        print("{}) {}".format(idx + 1, element))

    i = input("Enter number: ")
    try:
        if 0 < int(i) <= len(options):
            return int(i) - 1
    except:
        pass
    return None

def selection(activityPropertyList):
    nr = let_user_pick(activityPropertyList)
    selection = activityPropertyList[nr]
    print("You chose: " + selection)
    return selection

chosenStatus = selection(activityStatus)
chosenDurage = selection(activityDurage)
chosenLocation = selection(activityLocation)

print(chosenStatus)
print(chosenDurage)
print(chosenLocation)