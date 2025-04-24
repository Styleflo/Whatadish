import pandas as pd
import sqlite3
import random as rd

conn = sqlite3.connect('my_base.db')

df = pd.read_sql_query("select * from my_table", conn)
playable_df = df.copy()

def isEndOfData():
    if playable_df.empty:
        return True
    return False

def pickNewData():
    global playable_df  # pour modifier la variable globale

    if not isEndOfData():
        random_index = rd.choice(playable_df.index)
        chosen_row = playable_df.loc[random_index]

        playable_df = playable_df.drop(index=random_index)

        return chosen_row

def verifyAnswer(answer, nom):
    return nom.lower() == answer.lower()
