from ..options.socket_option import COMMANDS, COMMAND_OPTS, COMMAND_LENGTH
from ..commands.command import Command
from ..logger import get_logger
from halo import Halo
import socketio
import json
import click

logger = get_logger()
spinner = Halo(text='Receiving', spinner='dots')

class Socket(object):
    def __init__(self, url):
        self.command = Command()
        self.url = url
        self.status = 'disconnected'
        self.receive = False
        self.sio = socketio.Client()
        self.sio.on('connect', self.on_connect)


    def execute(self, command, params=None):
        command_list = COMMAND_OPTS[command] if command in COMMAND_OPTS else None
        options = self.command.parse_command_options(command_list, params)

        if command == 'connect':
            self.connect()
        elif command == 'disconnect':
            self.disconnect()
        elif command == 'emit':
            self.emit(options)
        elif command == 'on':
            self.on(options)

    def get_status(self):
        return self.status

    def on_connect(self):
        self.status = 'connected'
        logger.debug('connected');

    def on_message(self, msg):
        del self.sio.handlers[self.namespace][self.event]
        spinner.stop()
        click.echo_via_pager(json.dumps(msg))
        logger.debug('receive {}'.format(msg))


    def connect(self):
        self.sio.connect(self.url)

    def disconnect(self):
        self.sio.disconnect()
        self.status = 'disconnected'

    def emit(self, options):
        event = options.event
        data = options.data
        namespace = options.namespace or '/'
        try:
            data = json.loads(data)
        except ValueError:
            pass
        self.sio.emit(event, data, namespace)

    def on(self, options):
        self.event = options.event
        self.namespace = options.namespace or '/'
        self.sio.on(self.event, self.on_message, self.namespace)
        spinner.start()

    def terminate(self):
        spinner.stop()
