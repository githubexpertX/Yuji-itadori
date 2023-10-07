from yuji import app
import logging

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    filemode="a",
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
)


def main():
    app.run()
    app.send_message(-1001954317013, "I'm Now online")


if __name__ == "__main__":
    main()
