from ..completer.websocket_completer import WebSocketCompleter
from ..prompt.prompt import Prompt
from ..runner.websocket import WebSocket

class WebSocketPrompt(Prompt):

    def __init__(self, url):
        super().__init__(url, WebSocket(url), WebSocketCompleter())

