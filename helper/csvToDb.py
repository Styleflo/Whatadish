import pandas as pd
import sqlite3

# Charger le CSV
df = pd.read_csv("../static/Data/bd1.csv")

# Connexion à une base SQLite (créée si elle n'existe pas)
conn = sqlite3.connect("../my_base.db")

# Exporter le DataFrame dans la base sous forme de table
df.to_sql("my_table", conn, if_exists="replace", index=False)

conn.close()
