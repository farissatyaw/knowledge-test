from django.http import HttpResponse
from prometheus_client import generate_latest, CollectorRegistry, Counter, Gauge
from kafka import KafkaConsumer
import threading
import os
import json

# Create your views here.
kafka_conf = {
    'bootstrap_servers': os.getenv("KAFKA_BROKERS"),
    'auto_offset_reset': 'earliest',
}

total_size_gauge = Gauge('total_size_bytes', 'Total size of files')

def consume_kafka():
    consumer = KafkaConsumer('csv.fileSize', **kafka_conf)

    def consume():
        for message in consumer:
            try:
                data = json.loads(message.value.decode('utf-8'))
                total_size_gauge.inc(data['size'])  # Increase the total size gauge
            except Exception as e:
                print(f"Error processing message: {str(e)}")

    # Start Kafka message consumption in a separate thread
    kafka_thread = threading.Thread(target=consume)
    kafka_thread.daemon = True
    kafka_thread.start()

def prometheus_metrics(request):
    # Start consuming Kafka messages
    consume_kafka()

    # Get the Prometheus metrics in plaintext format
    data = generate_latest()
    return HttpResponse(data, content_type='text/plain; version=0.0.4')