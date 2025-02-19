import pandas as pd

chunk_size = 100

for chunk in pd.read_csv(
    "Sources/video_games.csv", chunksize = chunk_size, dtype={
            "Title": "category",
            "Metrics.Review Score" : "int16",
            "Length.All PlayStyles.Average" : "float16"
        }
):
    print("CHUNK : ",chunk.info(memory_usage="deep"))

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



