import requests
import json
import mysql.connector

#setting up mysql connection
try:
    mydb = mysql.connector.connect(host = 'localhost', user = 'root',password = '',database='productdb')
except mysql.connector.Error as e:
    print("Connector error ",e)


mycursor = mydb.cursor()

data = requests.get("https://dummyjson.com/products").text

data_info = json.loads(data)
for i in data_info['products']:
    print(str(i['title']))

