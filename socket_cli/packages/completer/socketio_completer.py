from ..options.socketio_option import COMMANDS, COMMAND_OPTS
from .completer import PromptCompleter


class SocketIOCompleter(PromptCompleter):
    def __init__(self, fuzzy=True):
        super().__init__(fuzzy, COMMANDS, COMMAND_OPTS)
