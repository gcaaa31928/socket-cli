from ..completer.socketio_completer import SocketIOCompleter
from ..prompt.prompt import Prompt
from ..runner.socketio import SocketIO


class SocketIOPrompt(Prompt):
    def __init__(self, url):
        super().__init__(url, SocketIO(url), SocketIOCompleter())
