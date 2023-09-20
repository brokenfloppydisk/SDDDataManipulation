import pandas as pd
import numpy as np
import process_data
import random as rand

df = process_data.filter_planet_and_date()

def filter_appearances(df: pd.DataFrame, lower: int, upper: int) -> pd.DataFrame:
    df_2 = df[(df["Appearances"] >= lower) & (df["Appearances"] <= upper)]
    return df_2
    
def get_main_char(df: pd.DataFrame) -> pd.DataFrame:
    potential_main = filter_appearances(df, 100, 300)
    potential_main = potential_main[potential_main["Alignment"] == "Good"]
    return potential_main

def get_neutral_char(df: pd.DataFrame) -> pd.DataFrame:
    potential_side = filter_appearances(df, 10, 100)
    potential_side = potential_side[potential_side["Alignment"] == "Neutral"]
    return potential_side
    
def get_main_villain() -> pd.DataFrame:
    potential_villains = filter_appearances(df, 100, 300)
    potential_villains = potential_villains[potential_villains["Alignment"] == "Bad"]
    return potential_villains

def get_side_villain(df: pd.Dataframe) -> pd.DataFrame:
    potential_side_villain = filter_appearances(df, 1100, 300)
    potential_side_villain = potential_side_villain[potential_side_villain["Alignment"] ]

potential_main = get_main_char(df)
potential_villains = get_main_villain(df)

main_character = potential_main.sample()

good_freq = 0
evil_freq = 0


