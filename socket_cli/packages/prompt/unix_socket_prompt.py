from ..completer.unix_socket_completer import UnixSocketCompleter
from ..prompt.prompt import Prompt
from ..runner.unix_socket import UnixSocket

class UnixSocketPrompt(Prompt):

    def __init__(self, path):
        super().__init__(path, UnixSocket(path), UnixSocketCompleter())


