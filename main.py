import pandas as pd
import numpy as np
import process_data

df = process_data.filter_planet_and_date()

def filter_appearances(df: pd.DataFrame, lower: int, upper: int) -> pd.DataFrame:
    df_2 = df[(df["Appearances"] >= lower) & (df["Appearances"] <= upper)]
    return df_2
    
def get_main_char(df: pd.DataFrame) -> pd.DataFrame:
    potential_main = filter_appearances(df, 100, 300)
    potential_main = potential_main[potential_main["Alignment"] == "Good"]
    return potential_main
    
def get_main_villain() -> pd.DataFrame:
    potential_villains = filter_appearances(df, 100, 300)
    potential_villains = potential_villains[potential_villains["Alignment"] == "Bad"]
    return potential_villains

potential_main = get_main_char(df)
potential_villains = get_main_villain(df)

for index, row in potential_main.iterrows():
    pass

