from confluent_kafka import Producer
import serial
from datetime import datetime
import pytz

# Set up the serial connection (adjust settings as per your TIC hardware)
ser = serial.Serial("COM18", 115200, timeout=1)

# Set up Kafka producer
producer = Producer({"bootstrap.servers": "172.16.18.190:9092"})


# Set IST timezone
ist = pytz.timezone("Asia/Kolkata")


def send_to_kafka(data):
    producer.produce("tic-data-topic", data)
    producer.flush()


def collect_tic_data():
    while True:
        line = ser.readline().decode("utf-8").strip()
        if line:
            # Get the current time in IST and format it
            timestamp = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")
            data_with_timestamp = f"{timestamp}: {line}"
            print(f"Collected data: {data_with_timestamp}")
            send_to_kafka(data_with_timestamp)


if __name__ == "__main__":
    collect_tic_data()
