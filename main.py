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
consolidated_raw_data = "dados_consolidados"

mycursor.execute(f"SHOW TABLES LIKE '{consolidated_raw_data}'")
table_exists = mycursor.fetchone()

if table_exists:
    mycursor.execute(f"DROP TABLE {consolidated_raw_data}")

mycursor.execute(f"CREATE TABLE {consolidated_raw_data} (month VARCHAR(7), rake DOUBLE, players INT, rake_cash_game DOUBLE, rake_tournament DOUBLE, players_cash_game INT, tournament_players INT)")

# Consolidating data by month:
consolidated_df = df.groupby(df['access_datetime'].str.slice(0, 7)).agg({

