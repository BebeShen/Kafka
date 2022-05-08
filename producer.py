import json
from datetime import datetime
from kafka import KafkaProducer
from kafka.errors import KafkaError

def serializer(m):
    return json.dumps(m).encode()

producer = KafkaProducer(
    bootstrap_servers = ["localhost:29092"],
    api_version = (0,11,5),
    value_serializer = serializer
)

# futureRemoteMetadata = producer.send("my-first-topic", b'This is a message from Python script')
futureRemoteMetadata = producer.send("test-topic", key=serializer('key') , value={'Hello': 'This is a message from Python script'})
print(futureRemoteMetadata)

try:
    recordMetadata = futureRemoteMetadata.get(timeout=10)
    print(recordMetadata)
except KafkaError:
    pass

print(recordMetadata.topic)
print(recordMetadata.partition)
print(recordMetadata.offset)

for i in range(5):
    print("test")
    data = {'num': i, 'ts': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    producer.send('test-topic', key=serializer('test'), value=data)