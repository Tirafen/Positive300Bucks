broker_url = 'amqp://guest:guest@localhost:5672'
#backend_url = 'db+postgresql+psycopg2://postgres:Q1w2e3r4t5@127.0.0.1/test_db'
result_backend = 'db+postgresql+psycopg2://postgres:Q1w2e3r4t5@127.0.0.1/test_db'
backend_url = 'amqp://guest:guest@localhost:5672'

celery_track_started = True
celery_concurrency = 2
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['application/json']

task_queues = {"orders":
    {
        "exchange": "orders",
        "exchange_type": "direct",
        "binding_key": "order"
    }
}
task_default_exchange = "orders"
task_default_exchange_type = "direct"
task_default_routing_key = "order"
