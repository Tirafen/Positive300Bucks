from time import sleep
from kombu import Queue, Exchange
from celery import Celery

app = Celery('tasks')
celery_config = app.config_from_object('celeryconfig')
celery_queues = (Queue('orders', Exchange('orders', type='direct'), routing_key='order'))
app.autodiscover_tasks()


@app.task(exchange='orders', queue='orders')
def make_coffee(order_number, coffee_type):
    print(f"Получен заказ №{order_number}, тип - {coffee_type}")
    if coffee_type == "cappuccino":
        work_time = 20
    elif coffee_type == "americano":
        work_time = 10
    else:
        return "Wrong type"

    sleep(work_time)
    return f"Order {order_number} ready"

