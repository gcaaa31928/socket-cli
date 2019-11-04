from .socketio_prompt import SocketIOPrompt
from .websocket_prompt import WebSocketPrompt
from .unix_socket_prompt import UnixSocketPrompt
from urllib.parse import urlparse


def CreatePrompt(type, path):
    url = urlparse(path)
    scheme = url.scheme
    if type is None:
        if scheme == "http" or scheme == "https":
            return SocketIOPrompt(path)
        elif scheme == "ws" or scheme == "wss":
            return WebSocketPrompt(path)
        else:
            return UnixSocketPrompt(path)
    else:
        if type == "websocket":
            return WebSocketPrompt(path)
        elif type == "socketio":
            return SocketIOPrompt(path)
        elif type == "unix":
            return UnixSocketPrompt(path)
