import pika
from time import sleep

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='orders', exchange_type='direct', durable=True)
result = channel.queue_declare(queue='orders', durable=True)
channel.queue_bind(exchange='orders', queue='orders')

print(' [*] Waiting for orders. To exit press CTRL+C')


def callback(ch, method, properties, body):
    #print(" [x] Received %r" % body.decode())
    #sleep(body.count(b'.'))
    #print(" [x] Done")
    print(body)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='orders', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
