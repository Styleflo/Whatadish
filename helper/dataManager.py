import pandas as pd
import sqlite3
import random as rd
from geopy.distance import geodesic

with sqlite3.connect("my_base.db") as conn:
    df = pd.read_sql_query("select * from my_table", conn)
    playable_df = df.copy()

def isEndOfData():
    if playable_df.empty:
        return True
    return False

def pickNewData():
    global playable_df  # pour modifier la variable globale

    if not isEndOfData():
        chosen_row = playable_df.sample(1)
        playable_df.drop(index=chosen_row.index, inplace=True)
        return chosen_row.iloc[0]

def verifyAnswer(answer, nom):
    return nom.lower() == answer.lower()

def geo_proximity(coordinates, max_distance=8000):
    coord1 = coordinates[0]
    coord2 = coordinates[1]
    distance = geodesic(coord1, coord2).km
    proximity = 1 - min(distance / max_distance, 1)
    return round(proximity * 100, 2)

def proximity_percentage(userCountry, answerCountry):
    with sqlite3.connect("my_base.db") as conn:
        df = pd.read_sql_query("select CapitalLatitude, CapitalLongitude from CountryTable where CountryName= ?", conn, params=(userCountry,))
        df2 = pd.read_sql_query("select CapitalLatitude, CapitalLongitude from CountryTable where CountryName= ?", conn, params=(answerCountry,))

        if not df.empty and not df2.empty:
            latUserCountry = df.iloc[0]['CapitalLatitude']
            longUserCountry = df.iloc[0]['CapitalLongitude']
            latAnswerCountry = df2.iloc[0]['CapitalLatitude']
            longAnswerCountry = df2.iloc[0]['CapitalLongitude']
            return geo_proximity([(latUserCountry, longUserCountry), (latAnswerCountry, longAnswerCountry)])
        else:
            print("Un ou les deux pays ne sont pas trouvés dans la base de données.")

def isCountry(userCountry):
    with sqlite3.connect("my_base.db") as conn:
        df = pd.read_sql_query("select CountryName from CountryTable where CountryName= ?", conn, params=(userCountry,))
        if not df.empty:
            return True
        return False
