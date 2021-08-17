from time import time
from tasks import make_coffee
import random

coffee = ("americano", "cappuccino")
coffee_type = random.choice(coffee)
for i in range(1, 20):
    job = make_coffee.apply_async(args=[i, coffee_type])
    print(f"{time()}, {job.get()}")
    print(f"{time()}, {job.ready()}")




