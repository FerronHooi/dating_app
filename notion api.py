import requests, json

token = 'YOUR-SECRET-NOTION-INTEGRATION-TOKEN'

databaseId = "10f26e397f9c4b6da70d310139e5cd02"

headers = {
    "Authorization": "Bearer " + "secret_qPFAJQ6ZxhHPh6CqtqjBn9NV8ot2uABtAQvrCuLW05R",
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

# TODO: loop through all the results [0][1] and get the name of the activity

dictLol = {}

def readDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    #loop through all the result in the data dictionary and get all the activity names and append them to the list
    for i in data['results']:
        print(i)
        activityName = i['properties']['Name']['title'][0]['text']['content']
        print(activityName)

readDatabase(databaseId, headers)
