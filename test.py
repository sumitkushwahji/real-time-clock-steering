import time
import random

import serial
from confluent_kafka import Producer

# Set up Kafka producer
producer = Producer({"bootstrap.servers": "localhost:9092"})


def send_to_kafka(data):
    producer.produce("tic-data-topic", data)
    producer.flush()


def collect_tic_data(test_mode=False):
    if test_mode:
        # Generate random data for testing
        test_data = ["TIC001", "TIC002", "TIC003", "TIC004", "TIC005"]
        while True:
            data = random.choice(test_data)
            print(f"Test data: {data}")
            send_to_kafka(data)
            time.sleep(1)  # Add delay between sending data
    else:
        # Set up the serial connection (adjust settings as per your TIC hardware)
        ser = serial.Serial("COM3", 9600, timeout=1)
        while True:
            line = ser.readline().decode("utf-8").strip()
            if line:
                print(f"Collected data: {line}")
                send_to_kafka(line)


if __name__ == "__main__":
    # Set test_mode=True to send random data for testing
    collect_tic_data(test_mode=True)
