import pandas as pd

# Büyük bir CSV dosyasını okuma
df = pd.read_csv("Sources/video_games.csv")

# İlk 5 satırı göster
print(df.head())

# Veri çerçevesinin genel bilgilerini göster
print(df.info())

# Hızlı istatistiksel analiz
print(df.describe())

