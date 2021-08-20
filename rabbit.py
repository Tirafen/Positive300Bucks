import pika


def send_order_to_queue(order):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='orders', exchange_type='direct', durable=True)

    message = ''.join(str(order))

    channel.basic_publish(exchange='orders', routing_key='order', body=message)
    print(" [x] Sent %r" % message)
    connection.close()