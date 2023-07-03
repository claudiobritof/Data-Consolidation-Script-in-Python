import mysql.connector
import pandas as pd

#Accessing database and generating a cursor to interact with it:
db = mysql.connector.connect(
    host="40b8f30251.nxcli.io",
    user="a4f2b49a_padawan",
    passwd="KaratFlanksUgliedSpinal",
    database="a4f2b49a_sample_database"
)

mycursor = db.cursor()

#Selecting data from 'raw_data' table:
mycursor.execute("SELECT * FROM raw_data")

