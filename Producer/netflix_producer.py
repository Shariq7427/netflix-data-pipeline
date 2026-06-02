from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

movies = [
    "Stranger Things",
    "Wednesday",
    "Dark",
    "Money Heist",
    "The Witcher"
]

while True:
    event = {
        "user_id": random.randint(1000,9999),
        "movie": random.choice(movies),
        "watch_time": random.randint(10,180)
    }

    producer.send("netflix-events", event)
    print(event)

    time.sleep(2)