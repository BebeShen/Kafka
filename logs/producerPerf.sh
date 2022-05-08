echo `date +"%Y-%m-%d %H:%M" -d "+8 hours"` >> ../../log/producerPerf.log
# kafka producer perf
kafka-producer-perf-test --topic my-first-topic --num-records 100000 --throughput 20000 --record-size 1024 --producer-props batch.size=1 linger.ms=5000 acks=1 compression.type=gzip bootstrap.servers=localhost:9092 >> ../../log/producerPerf.log