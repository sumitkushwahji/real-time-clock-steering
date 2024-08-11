from confluent_kafka import Producer
import serial

# Set up the serial connection (adjust settings as per your TIC hardware)
ser = serial.Serial('COM3', 9600, timeout=1)

# Set up Kafka producer
producer = Producer({'bootstrap.servers': 'localhost:9092'})

def send_to_kafka(data):
    producer.produce('tic-data-topic', data)
    producer.flush()

def collect_tic_data():
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print(f"Collected data: {line}")
            send_to_kafka(line)

if __name__ == "__main__":
    collect_tic_data()
