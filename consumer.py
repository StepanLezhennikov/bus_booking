from aiokafka import AIOKafkaConsumer


async def consume_message(topic: str):
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers='localhost:9092',
        group_id="booking"
    )
    await consumer.start()
    try:
        async for message in consumer:
            print(f"Полученное сообщение: {message.value.decode('utf-8')}")
    finally:
        await consumer.stop()

