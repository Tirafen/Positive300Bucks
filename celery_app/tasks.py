from time import sleep
from celery import Celery
from celery_app.database import SessionLocal
from sqlalchemy import text
from celery_app import celeryconfig

db = SessionLocal()

app = Celery('tasks')
celery_config = app.config_from_object(celeryconfig)

app.conf.beat_schedule = {
    'check_orders': {
        'task': 'tasks.get_order_from_db',
        'schedule': 5,
    },
}


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5.0, get_order_from_db.s(), name='every 10')


@app.task(exchange='orders', queue='orders')
def get_order_from_db():
    order = db.execute(text("SELECT order_number, coffee_type FROM orders WHERE wait='true'")).first()
    if order is None:
        print("Нет заказов в очереди")
    else:
        print(f"Отправлен в работу заказ {order[0]}, кофе - {order[1]}")
        return make_coffee(order)


@app.task(exchange='orders', queue='orders')
def make_coffee(order):  # Главный таск
    order_number = order[0]
    coffee_type = order[1]
    print(f"Получен заказ №{order_number}, тип - {coffee_type}")
    order_progress = text("UPDATE orders SET in_progress='true', wait='false' WHERE order_number=:y")
    order_progress = order_progress.bindparams(y=f"{order_number}")
    db.execute(order_progress)
    db.commit()
    db.close()
    if coffee_type == "cappuccino":
        work_time = 20
    elif coffee_type == "americano":
        work_time = 10
    else:
        return "Wrong type"
    sleep(work_time)
    order_ready = text("UPDATE orders SET ready='true', in_progress='false' WHERE order_number=:z")
    order_ready = order_ready.bindparams(z=f"{order_number}")
    db.execute(order_ready)
    db.commit()
    db.close()
    print(f"Заказ {order_number} готов")
    return f"Заказ {order_number} готов"


app.autodiscover_tasks()


# celery -A tasks worker --concurrency=1 -n worker1@%h
# celery -A tasks worker --concurrency=1 -n worker2@%h
# celery -A tasks beat
