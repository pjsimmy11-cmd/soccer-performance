from pathlib import Path

import kagglehub
from kagglehub import KaggleDatasetAdapter

file_name = "players_data_light-2025_2026.csv"

df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "hubertsidorowicz/football-players-stats-2025-2026",
    file_name,
)

Path("data").mkdir(exist_ok=True)

df.to_csv(
    Path("data") / file_name,
    index=False
)

print("Dataset downloaded successfully!")
print(df.head())
