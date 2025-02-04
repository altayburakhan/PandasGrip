import pandas as pd

df = pd.read_csv("Sources/video_games.csv")

print(df.head())
print(df.info())
print(df.describe())

