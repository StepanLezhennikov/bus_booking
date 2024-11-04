from aiokafka import AIOKafkaProducer


async def send_message(topic: str, message: str):
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9092'
    )
    await producer.start()
    try:
        await producer.send_and_wait(topic, message.encode('utf-8'))
    finally:
        await producer.stop()
