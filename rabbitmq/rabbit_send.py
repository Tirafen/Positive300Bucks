import pika
import sys


def rabbit_send(order_number: int, coffee_type: str):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='orders', exchange_type='direct', durable=True)

    message = f"{order_number} {coffee_type}" or "No orders in queue"
    channel.basic_publish(exchange='orders', routing_key='orders', body=message)
    print(" [x] Sent %r" % message)
    connection.close()

