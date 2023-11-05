import os

from config import QUEUE, connection


def list_queues():
    print(os.system("docker exec -it rabbitmq rabbitmqctl list_queues"))


def publish_message():
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE)

    channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")

    connection.close()


if __name__ == "__main__":
    publish_message()
