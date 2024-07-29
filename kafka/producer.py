# Imports
import requests
import json
import time
import yaml
from kafka import KafkaProducer

# Load configuration
with open('configuration.yaml', 'r') as file:
    config = yaml.safe_load(file)

api_url = config['api']['url']
batch_size = config['api']['batch_size']
kafka_topic = config['kafka']['topic']
kafka_servers = config['kafka']['bootstrap_servers']

# Set up Kafka producer
producer = KafkaProducer(
    bootstrap_servers=kafka_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def fetch_data(url, batch_size):
    response = requests.get(url, params={'$limit': batch_size})
    data = response.json()
    return data

if __name__ == "__main__":
    while True:
        data = fetch_data(api_url, batch_size)
        if data:
            for record in data:
                producer.send(kafka_topic, record)
            print(f"Produced {len(data)} records to Kafka topic {kafka_topic}")
        time.sleep(60)
