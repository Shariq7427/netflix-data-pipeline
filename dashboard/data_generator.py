import pandas as pd
import numpy as np

np.random.seed(42)

titles = [
    "Stranger Things",
    "Money Heist",
    "Wednesday",
    "The Witcher",
    "Bridgerton"
]

genres = ["Drama", "Thriller", "Comedy", "Action", "Documentary"]
countries = ["United States", "India", "Brazil", "United Kingdom", "Canada"]
devices = ["Mobile", "TV", "Desktop", "Tablet"]

rows = []

for _ in range(5000):
    rows.append({
        "title": np.random.choice(titles),
        "genre": np.random.choice(genres),
        "country": np.random.choice(countries),
        "device": np.random.choice(devices),
        "watch_time": np.random.randint(20,120),
        "completion_rate": np.random.uniform(50,100)
    })

df = pd.DataFrame(rows)
df.to_csv("netflix_dashboard_data.csv", index=False)

print("Dataset Generated")