import pandas as pd


df = pd.read_csv("Sources/video_games.csv")
print(df.info(memory_usage="deep"))


# Optimized version

df = pd.read_csv("Sources/video_games.csv",
                 dtype={
                     "Title": "category",
                     "Metrics.Review Score" : "int16",
                     "Length.All PlayStyles.Average" : "float16"
                 })

print(df.info(memory_usage="deep"))


