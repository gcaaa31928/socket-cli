from ..options.websocket_option import COMMANDS, COMMAND_OPTS
from ..commands.command import Command
from .runner import Runner
import asyncio
import websockets
import click
import json


class WebSocket(Runner):
    def __init__(self, url):
        super().__init__(url)

    def execute(self, command, params=None):
        command_list = COMMAND_OPTS[command] if command in COMMAND_OPTS else None
        options = self.command.parse_command_options(command_list, params)

        self.loop = asyncio.get_event_loop()
        if command == "connect":
            self.loop.run_until_complete(self.connect())
        elif command == "send":
            self.loop.run_until_complete(self.send(options))
        elif command == "recv":
            self.loop.run_until_complete(self.recv())

    def get_status(self):
        return self.status

    async def recv(self):
        self.spinner.start()
        result = await self.websocket.recv()
        self.spinner.stop()
        click.echo_via_pager(json.dumps(result))

    async def send(self, options):
        result = await self.websocket.send(options.data)

    async def connect(self):
        self.websocket = await websockets.connect(self.url)
        self.status = "connected"

    def stop(self):
        if not hasattr(self, "loop"):
            return
        self.loop.stop()
        self.spinner.stop()
