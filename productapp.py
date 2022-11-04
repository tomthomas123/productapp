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
    price = str(i['price'])
    discout = str(i['discountPercentage'])
    rating = str(i['rating'])
    stock = str(i['stock'])
    sql = 'INSERT INTO `products`(`title`, `description`, `price`, `discount`, `rating`, `stock`, `brand`, `category`) VALUES ("'+i['title']+'","'+i['description']+'", "'+price+'","'+discout+'","'+rating+'","'+stock+'","'+i['brand']+'","'+i['category']+'")'
    mycursor.execute(sql)
    mydb.commit()
    print(str(i['title']))

