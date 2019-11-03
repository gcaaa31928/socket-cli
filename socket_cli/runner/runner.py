from ..logger import get_logger
from ..commands.command import Command
from halo import Halo

class Runner(object):
    def __init__(self, url):
        self.command = Command()
        self.url = url
        self.status = 'disconnected'
        self.receive = False
        self.spinner = Halo(text='Receiving', spinner='dots')
        self.logger = get_logger()

    def execute(self, command, params=None):
        pass

    def get_status(self):
        return self.status

    def stop(self):
        self.spinner.stop()

    def terminate(self):
        self.stop()
