import pandas as pd
import numpy as np
from typing import Tuple
import process_data

df = process_data.filter_planet_and_date()

def filter(df: pd.DataFrame, lower: int=None, upper: int=None, alignment: str=None, identity: str=None, year: int=None) -> pd.DataFrame:
    df_2 = df
    if lower or upper:
        df_2 = df_2[(df_2["Appearances"] >= lower) & (df_2["Appearances"] <= upper)]
    if alignment:
        df_2 = df_2[df_2["Alignment"] == alignment]
    if identity:
        df_2 = df_2[(df_2["Identity"] == identity)]
    if year:
        df_2 = df_2[(df_2["First_appeared"] >= year - 30) & (df_2["First_appeared"] <= year + 30)]
    return df_2

def get_freq(df: pd.DataFrame):
    return sum(value for (index,value) in df["Appearances"].items())

#  Filter the frequencies and alignments for each group
pot_main = filter(df, lower=100, upper=300, alignment="Good", identity="Secret")

# Get main character
main_character: pd.DataFrame = pot_main.sample()

# Get other characters in same time period as chosen year
chosen_year = main_character["First_appeared"].item()
pot_vil       = filter(df, lower=100, upper=300, alignment="Bad", identity="Secret", year=chosen_year) 
pot_side_neut = filter(df, lower=10,  upper=100, alignment="Neutral", year=chosen_year)
pot_side_good = filter(df, lower=10,  upper=100, alignment="Good", year=chosen_year)
pot_side_bad  = filter(df, lower=10,  upper=100, alignment="Bad", year=chosen_year)

# Get main character, main villain, and side character
main_villain: pd.DataFrame = pot_vil.sample()
side_good_1: pd.DataFrame = pot_side_good.sample(n=2)
side_good_2: pd.DataFrame = pot_side_good.sample(n=2)
side_good = pd.concat([side_good_1, side_good_2])

# # Calculate all frequencies 
# def get_freq(df: pd.DataFrame) -> int:
#     return sum(value for (index, value) in df["Appearances"].items())

#  Calculate frequencies
good_freq = main_character["Appearances"].item() + get_freq(side_good)

good_freq_1_2 = main_character["Appearances"].item() + get_freq(side_good_1)
good_freq_3_5 = main_character["Appearances"].item() + get_freq(side_good_2)

main_villain_freq = main_villain["Appearances"].item()

# Filters appearances of potential bad to ensure a balance in frequencies between bad and good chars
# Lowest num of appearances is 10
# Highest num of appearaches is the total of good frequencies subtracted by the current frequency of evil characters

pot_side_bad_1_2 = filter(pot_side_bad, lower=(good_freq_1_2 - main_villain_freq)/2 - 20, upper=(good_freq_1_2 - main_villain_freq)/2 + 20)


side_bad_1: pd.DataFrame = pot_side_bad_1_2.sample(n=2)

side_bad_2: pd.DataFrame = pot_side_bad_1_2.sample(n=2)

pot_side_bad_3_5 = filter(pot_side_bad, lower=(good_freq_3_5 - main_villain_freq)/2 - 20, upper=(good_freq_3_5 - main_villain_freq)/2 + 20)



side_bad_3: pd.DataFrame = pot_side_bad_1_2.sample(n=2)
side_bad_4: pd.DataFrame = pot_side_bad_1_2.sample(n=2)
side_bad_5: pd.DataFrame = pot_side_bad_1_2.sample(n=2)

# Update evil frequencies
evil_freq = main_villain_freq + get_freq(side_bad_1) + get_freq(side_bad_2) + get_freq(side_bad_3) + get_freq(side_bad_4) + get_freq(side_bad_5)

# Find neutral characters
side_neut: pd.DataFrame = pot_side_neut.sample(n=25)

def to_string(char: pd.DataFrame) -> str:
    names =     [value for (index, value) in char['Name'].items()]
    identity =  [value for (index, value) in char['Identity'].items()]
    alignment = [value for (index, value) in char['Alignment'].items()]
    alive =     [value for (index, value) in char['Alive'].items()]
    frequency = [value for (index, value) in char['Appearances'].items()]
    planet =    [value for (index, value) in char['Planet'].items()]
    
    output_str = ""

    for index in range(len(names)):
        output_str += f"{names[index] :<20}"
        output_str += f"{identity[index] :<30}"
        output_str += f"{alignment[index] :<10}"
        output_str += f"{alive[index] :<5}"
        output_str += f"{frequency[index] :<5}"
        output_str += f"{planet[index] :<10}\n"

    return output_str 

# Debug prints


all_bad = pd.concat([main_villain, side_bad_1, side_bad_2, side_bad_3, side_bad_4, side_bad_5])
side_bad = pd.concat([side_bad_1, side_bad_2, side_bad_3, side_bad_4, side_bad_5])

output  = f"Good frequency: {good_freq}\n"
output += f"Bad frequency: {evil_freq}\n\n"
output += f"Good frequency for first and second movie: {good_freq_1_2}\n"
output += f"Bad frequency for first movie: {get_freq(side_bad_1) + main_villain_freq}\n"
output += f"Bad frequency for second movie: {get_freq(side_bad_2) + main_villain_freq}\n\n"
output += f"Good frequency for third to fifth movie: {good_freq_3_5}\n"
output += f"Bad frequency for third movie: {get_freq(side_bad_3) + main_villain_freq}\n"
output += f"Bad frequency for fourth movie: {get_freq(side_bad_4) + main_villain_freq}\n"
output += f"Bad frequency for last movie: {get_freq(side_bad_5) + main_villain_freq}\n\n"

output += f"Main charater: \n{to_string(main_character)}\n"
output += f"Main villain: \n{to_string(main_villain)}\n"
output += f"Side good: \n{to_string(side_good)}\n"
output += f"Side bad: \n{to_string(side_bad)}\n"
output += f"Side neut: \n{to_string(side_neut)}\n"

print(output)

with open("Characters.txt", 'w') as f:
    f.write(output)



