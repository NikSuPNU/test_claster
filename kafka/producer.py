import kafka
import time
import random

def main():
    i = 0
    producer = kafka.KafkaProducer(bootstrap_servers='localhost:29092')
    while True:
        producer.send('test_topik', (f'some_message_bytes_{str(i)}'.encode('utf-8')))
        time.sleep(random.randint(1, 40))
        producer.flush()
        i += 1

if __name__ == '__main__':
    main()