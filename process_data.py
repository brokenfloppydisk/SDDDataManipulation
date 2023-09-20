import pandas as pd

def filter_planet_and_date() -> pd.DataFrame:
    df: pd.DataFrame = pd.read_csv('comic_characters.csv')

    # Simplifies the First_appeared column to only the year in which the characters first appeared (without the month)
    df['First_appeared'] = df['First_appeared'].str.extract(pat='(\d{4})')
    df["First_appeared"] = df["First_appeared"].astype(int)

    # print(df.head(5))

    # Filters the data frame so the characters are only from New Earth (DC) and Earth-616 (Marvel)
    test = df[(df["Planet"] != "Earth-616") & (df["Planet"] != "New Earth")].index
    df.drop(test)

    df.to_csv('filtered.csv', sep=',', index=False,header=True)

    df["First_appeared"] = df["First_appeared"].astype(int)

    return df

if __name__ == "__main__":
    filter_planet_and_date()