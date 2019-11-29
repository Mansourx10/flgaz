import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'reporting',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx.close()