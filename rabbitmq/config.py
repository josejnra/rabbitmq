import pika

QUEUE = "my-queue"


credentials = pika.PlainCredentials(username="user", password="pass")
conn_parameters = pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)

connection = pika.BlockingConnection(conn_parameters)
