import pandas as pd

def filter_planet_and_date() -> pd.DataFrame:
    df: pd.DataFrame = pd.read_csv('comic_characters.csv')

    df['First_appeared'] = df['First_appeared'].str.extract(pat='(\d{4})')

    print(df.head(5))

    test = df[(df["Planet"] != "Earth-616") & (df["Planet"] != "New Earth")].index
    df.drop(test)

    df.to_csv('filtered.csv', sep=',', index=False,header=True)

    return df

if __name__ == "__main__":
    filter_planet_and_date()