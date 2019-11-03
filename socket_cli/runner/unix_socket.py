from ..options.websocket_option import COMMANDS, COMMAND_OPTS, COMMAND_LENGTH
from ..commands.command import Command
from .runner import Runner
import asyncio
import websockets
import click
import json
import socket

BUFF_SIZE=1024

class UnixSocket(Runner):
    def __init__(self, path):
        self.path = path
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        super().__init__(path)

    def execute(self, command, params=None):
        command_list = COMMAND_OPTS[command] if command in COMMAND_OPTS else None
        options = self.command.parse_command_options(command_list, params)

        if command == 'connect':
            self.connect()
        elif command == 'send':
            self.send(options)

    def get_status(self):
        return self.status

    def send(self, options):
        self.sock.sendall(options.data.encode('utf-8'))
        result = self.recvall()
        print(result)

    def connect(self):
        self.sock.connect(self.path)
        self.status = 'connected'

    def recvall(self):
        data = b''
        while True:
            recv_data = self.sock.recv(BUFF_SIZE)
            data += recv_data
            if len(recv_data) < BUFF_SIZE:
                break
        return data

    def stop(self):
        pass
