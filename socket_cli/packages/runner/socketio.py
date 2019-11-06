from ..options.socketio_option import COMMANDS, COMMAND_OPTS
from ..commands.command import Command
from .runner import Runner
import socketio
import json
import click
import asyncio


class SocketIO(Runner):
    def __init__(self, url):
        super().__init__(url)
        self.sio = socketio.Client()
        self.sio.on("connect", self.on_connect)

    def execute(self, command, params=None):
        command_list = COMMAND_OPTS[command] if command in COMMAND_OPTS else None
        options = self.command.parse_command_options(command_list, params)
        if command == "connect":
            self.connect(options)
        elif command == "emit":
            self.emit(options)
        elif command == "on":
            self.on(options)

    def on_connect(self):
        self.status = "connected"
        self.logger.debug("connected")

    def on_message(self, msg):
        del self.sio.handlers[self.namespace][self.event]
        self.spinner.stop()
        click.echo_via_pager(json.dumps(msg))
        self.logger.debug("receive {}".format(msg))

    def connect(self, options):
        self.namespace = options.namespace or "/"
        self.sio.connect(self.url, namespaces=[self.namespace])

    def disconnect(self):
        self.sio.disconnect()
        self.status = "disconnected"

    def emit(self, options):
        event = options.event
        data = options.data
        namespace = options.namespace or "/"
        try:
            data = json.loads(data)
        except ValueError:
            pass
        self.sio.emit(event, data, namespace)

    def on(self, options):
        self.event = options.event
        self.namespace = options.namespace or "/"
        self.sio.on(self.event, self.on_message, self.namespace)
        self.spinner.start()

    def stop(self):
        super().stop()

    def terminate(self):
        super().terminate()
        self.sio.disconnect()
