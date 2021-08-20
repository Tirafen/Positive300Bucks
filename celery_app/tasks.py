from time import sleep
from kombu import Queue, Exchange
from celery import Celery, Task
from database import SessionLocal
from sqlalchemy import text
from rabbit import send_order_to_queue
import celeryconfig

# FIXME пофиксить импорт модулей в воркера
db = SessionLocal()


class SqlAlchemyTask(Task):  # TODO убрать, если не работает
    abstract = True

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        db.remove()


app = Celery('tasks')
celery_config = app.config_from_object(celeryconfig)
celery_queues = (Queue('orders', Exchange('orders', type='direct'), routing_key='order'))


# TODO Скорее всего убрать, дублируется из конфига


@app.task(base=SqlAlchemyTask)
def get_order_from_db():
    order = db.execute(text("SELECT order_number, coffee_type FROM orders WHERE wait = 'true'")).first()
    return send_order_to_queue(order)


@app.task(exchange='orders', queue='orders')
def make_coffee(order_number, coffee_type):  # Главный таск
    print(f"Получен заказ №{order_number}, тип - {coffee_type}")
    if coffee_type == "cappuccino":
        work_time = 20
    elif coffee_type == "americano":
        work_time = 10
    else:
        return "Wrong type"

    sleep(work_time)
    return f"Order {order_number} ready"


app.autodiscover_tasks()
