import kafka
import time

def main():
    consumer = kafka.KafkaConsumer('test_topik', bootstrap_servers='localhost:29092')
    for message in consumer:
        print(message.value.decode('utf-8'))
        time.sleep(1)

if __name__ == '__main__':
    main()