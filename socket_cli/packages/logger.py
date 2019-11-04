import logging
import os

FORMAT = "%(asctime)s (%(process)d/%(threadName)s) %(name)s %(levelname)s - %(message)s"
logging.basicConfig(
    level=logging.DEBUG, filename=os.path.expanduser("~/.socket-cli.log"), format=FORMAT
)
logger = logging.getLogger("socket-cli")


def get_logger():
    return logger
