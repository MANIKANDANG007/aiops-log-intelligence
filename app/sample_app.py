import logging
import random
import time

logging.basicConfig(
    filename="/var/log/app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s service=payment %(message)s",
)

while True:
    if random.randint(1, 10) > 7:
        logging.error("DB connection timeout")
    else:
        logging.info("Payment processed successfully")
    time.sleep(2)
