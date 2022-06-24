import pyodbc
import pandas as pd
import csv

#convert csv column 'activity' to list
df = pd.read_csv('date_ideas.csv')
# date_ideas_list = df['Activity'].tolist()

server = 'serverdateapp.database.windows.net'
database = 'dateapplication'
username = 'ferronhooi'
password = 'OldSkool@95'
driver= '{ODBC Driver 18 for SQL Server}'

with open ('date_ideas.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    columns = next(reader)
    query = 'insert into da_activities({0}) values ({1})'
    query = query.format(','.join(columns), ','.join('?' * len(columns)))
    cursor = connection.cursor()
    for data in reader:
        cursor.execute(query, data)
    cursor.commit()

# #TODO: Fix query and find a way to enter all csv data at once instead of one by one
with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        # cursor.execute("LOAD DATA LOCAL INFILE '/date_ideas.csv' INTO TABLE da_activities ")
        for date_idea in df:
            cursor.execute("INSERT INTO da_activities (ActivityID, ActivityName) values (?, ?)", df['ActivityID'].tolist(), df['Activity'].tolist())
        cursor.execute("SELECT * FROM da_activities")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()

# "LOAD DATA INFILE '/path/to/my/file' INTO TABLE sometable FIELDS TERMINATED BY ';' ENCLOSED BY '\"' ESCAPED BY '\\\\'"