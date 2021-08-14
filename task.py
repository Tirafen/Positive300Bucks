from time import sleep
from celery_app import Celery
from celery_app.utils.log import get_task_logger

worker = Celery('tasks', broker='amqp://guest:guest@localhost:5672',
                backend='db+postgresql://postgres:Q1w2e3r4t5@127.0.0.1/test_db',
                include=['task'])

celery_log = get_task_logger(__name__)


@worker.task
def make_coffee(coffee_type):
    if coffee_type == "americano":
        prod_time = 10
    elif coffee_type == "cappuccino":
        prod_time = 20
    else:
        return Exception("Wrong coffee type")

    # TODO маркер начала выполнения
    sleep(prod_time)
    celery_log.info(f"Order Complete!")
    # TODO маркер окончания выполнения

