import mysql.connector
import pandas as pd

# Accessing database and generating a cursor to interact with it:
db = mysql.connector.connect(
    host="40b8f30251.nxcli.io",
    user="a4f2b49a_padawan",
    passwd="KaratFlanksUgliedSpinal",
    database="a4f2b49a_sample_database"
)

mycursor = db.cursor()

# Selecting data from 'raw_data' table:
mycursor.execute("SELECT * FROM raw_data")

results = mycursor.fetchall()

# Creating a DataFrame (pandas) with results:
df = pd.DataFrame(results, columns=[desc[0] for desc in mycursor.description])

# Saving consolidated data in another table (if table already exists, I remove it before to avoid duplicity):
consolidated_raw_data = "consolidated_data"

mycursor.execute(f"SHOW TABLES LIKE '{consolidated_raw_data}'")
table_exists = mycursor.fetchone()

if table_exists:
    mycursor.execute(f"DROP TABLE {consolidated_raw_data}")

mycursor.execute(f"CREATE TABLE {consolidated_raw_data} (month VARCHAR(7), rake DOUBLE, players INT, rake_cash_game DOUBLE, rake_tournament DOUBLE, cash_game_players INT, tournament_players INT)")

# Consolidating data by month:
consolidated_df = df.groupby(df['access_datetime'].str.slice(0, 7)).agg({
    'rake': 'sum',
    'customer_id': 'nunique',
    'modality': lambda x: x[x == 'cash game'].count(),
    'modality': lambda x: x[x == 'tournament'].count(),
    'customer_id': lambda x: x[x['modality'] == 'cash game'].nunique(),
    'customer_id': lambda x: x[x['modality'] == 'tournament'].nunique()
}).reset_index()

# Inserting consolidated data on table:

for index, row in consolidated_df.iterrows():
    mycursor.execute(f"INSERT INTO {consolidated_raw_data} (month, rake, players, rake_cash_game, rake_tournament, cash_game_players, tournament_players) VALUES (%s, %f, %d, %f, %f, %d, %d)", (row[' access_datetime'], row['rake'], row['customer_id'], row['modality_cash_game'], row['modality_tournament'], row['customer_id_cash game'], row['customer_id_tournament']))

#Commiting changes on database:
db.commit()
print(consolidated_raw_data)

#Closing connection with database:
db.close()
