from time import sleep
from kombu import Queue, Exchange
from celery import Celery

app = Celery('celery_app', include=['celery_app.tasks'])
celery_config = app.config_from_object('celeryconfig')
celery_queues = (Queue('orders', Exchange('celery_app', type='direct'), routing_key='order'))


@app.task(exchange='celery', queue='orders')
def make_coffee(order_number, coffee_type):
    if coffee_type == "cappuccino":
        work_time = 20
    elif coffee_type == "americano":
        work_time = 10
    else:
        return "Wrong type"

    sleep(work_time)
    return f"Order {order_number} ready"

