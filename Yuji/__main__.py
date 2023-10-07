from Yuji import app
import logging

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    filemode="a",
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
)


print("now im alive babe")

app.start()
