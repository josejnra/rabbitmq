import os
import sys

from config import QUEUE, connection


def callback(ch, method, properties, body):
    print(f"Message Received: {body}")


def consume_messages():
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE)

    channel.basic_consume(queue="hello", auto_ack=True, on_message_callback=callback)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        consume_messages()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
