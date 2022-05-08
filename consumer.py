import json
from kafka import KafkaConsumer

def value_deserializer(m):
    try:
        return json.loads(m.decode())
    except Exception:
        return {}

consumer = KafkaConsumer(
#    'my-first-topic',
   'test-topic',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='group-c',
    bootstrap_servers=['localhost:29092'],
    key_deserializer=value_deserializer,
    value_deserializer=value_deserializer
)

for m in consumer:
    print('%s:%d:%d: key=%s value=%s' % (
        m.topic,
        m.partition,
        m.offset,
        m.key,
        m.value
    ))