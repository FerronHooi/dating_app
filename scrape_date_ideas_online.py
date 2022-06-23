import pandas as pd
from bs4 import BeautifulSoup
import requests

linksCoupleInTheKitchen = ['https://coupleinthekitchen.com/summer-date-ideas/', 'https://coupleinthekitchen.com/splurge-date-ideas/', 'https://coupleinthekitchen.com/winter-date-ideas/', 'https://coupleinthekitchen.com/outdoor-date-ideas/', 'https://coupleinthekitchen.com/indoor-date-ideas/', 'https://coupleinthekitchen.com/group-date-ideas/', 'https://coupleinthekitchen.com/sober-date-ideas/']
linkSmartCouples = 'https://smartcouples.ifas.ufl.edu/dating/having-fun-and-staying-close/101-fun-dating-ideas/'
date_ideas_list = []

#scrape the website https://coupleinthekitchen.com/summer-date-ideas/ and save it as a csv file called summer_date_ideas.csv
def scrape_date_ideas(link, classname, column1, column2):
    requests.get(link)
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    date_ideas = soup.find_all(column1, class_=classname)
    for date_idea in date_ideas:
        #only append unique values to the list
        if date_idea.find(column2).get_text().strip() not in date_ideas_list:
            date_ideas_list.append(date_idea.find(column2).get_text().strip())

def date_ideas(links, classname, column1, column2):
    for link in links:
        scrape_date_ideas(link, classname, column1, column2)

#enter list of links at [0] and classname at [1]
date_ideas(linksCoupleInTheKitchen, 'sp-col-4 index-item', 'div', 'h2')

#write list to csv file column1 = Activity
df = pd.DataFrame(date_ideas_list , columns = ['Activity'])
df.to_csv('date_ideas.csv', index=False)

dfNotion = pd.read_csv('Dates 10f26e397f9c4b6da70d310139e5cd02.csv')
#append dfNotion ideas to csv and write to file
for index, row in dfNotion.iterrows():
    if row['Name'] not in date_ideas_list:
        date_ideas_list.append(row['Name'])
dfNotion = pd.DataFrame(date_ideas_list , columns = ['Activity'])
dfNotion.to_csv('date_ideas_notion.csv', index=False)

print(date_ideas_list)
