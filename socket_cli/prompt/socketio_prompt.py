from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import DynamicCompleter
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.data import JsonBareObjectLexer
from ..completer.socketio_completer import SocketIOCompleter
from ..logger import get_logger
from ..commands.command_options import CommandList, CommandOption
from ..utils.token import safe_split, split_command_and_args
from ..runner.socket import Socket
from ..options.socket_option import COMMANDS, COMMAND_OPTS, COMMAND_LENGTH
from halo import Halo

logger = get_logger()

PROMPT_STYLE = {
    # User input (default text).
    #'':          '#ff0066',
    # Prompt.
    'rprompt': 'bg:#ff0066 #ffffff',
    'status':   '#884444 bg:#444400',
    'colon':    '#0000aa',
    'shell':    '#00aa00',
    'host':     '#00ffff',
}


class SocketIOPrompt(object):

    def __init__(self, url):
        self.url = url
        self.socket = Socket(url)
        self.completer = SocketIOCompleter(url)
        self.prompt_session = PromptSession(
            lexer=PygmentsLexer(JsonBareObjectLexer),
            completer=DynamicCompleter(lambda: self.completer),
        )

    def get_prompt_message(self):
        message = [
            ('class:shell', '> '),
        ]
        return message

    def get_rprompt(self):
        return ' {} '.format(self.socket.get_status())

    def get_style(self):
        style = PROMPT_STYLE
        status = self.socket.get_status()
        if status == 'connected':
            style['rprompt'] = 'bg:#00ff00 #000000'
        elif status == 'disconnected':
            style['rprompt'] = 'bg:#ff0066 #ffffff'
        return Style.from_dict(style)

    def one_iteration(self, text=None):
        if text is None:
            try:
                text = self.prompt_session.prompt(self.get_prompt_message(), style=self.get_style(), rprompt=self.get_rprompt)
            except KeyboardInterrupt:
                spinner.stop()
                return
        if not text.strip():
            return
        try:
            tokens = safe_split(text) if text else ['']
            command, params, _ = split_command_and_args(tokens, COMMAND_LENGTH)
            self.socket.execute(command, params)
        except RuntimeError as e:
            return

    def run_cli(self):
        self.one_iteration()

