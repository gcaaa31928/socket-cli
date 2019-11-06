from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import DynamicCompleter
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from pygments.lexers.data import JsonBareObjectLexer
from ..completer.completer import PromptCompleter
from ..logger import get_logger
from ..commands.command_options import CommandList, CommandOption
from ..utils.token import safe_split, split_command_and_args
from halo import Halo
import os

logger = get_logger()

PROMPT_STYLE = {
    # Prompt.
    "rprompt": "bg:#ff0066 #ffffff",
    "status": "#884444 bg:#444400",
    "colon": "#0000aa",
    "shell": "#00aa00",
    "host": "#00ffff",
}


class Prompt(object):
    def __init__(self, url, runner, completer):
        self.runner = runner
        self.completer = completer
        self.prompt_session = PromptSession(
            lexer=PygmentsLexer(JsonBareObjectLexer),
            completer=DynamicCompleter(lambda: self.completer),
            history=FileHistory(os.path.expanduser("~/.socket-cli.history")),
        )

    def get_prompt_message(self):
        message = [
            ("class:shell", "> "),
        ]
        return message

    def get_rprompt(self):
        return " {} ".format(self.runner.get_status())

    def get_style(self):
        style = PROMPT_STYLE
        status = self.runner.get_status()
        if status == "connected":
            style["rprompt"] = "bg:#00ff00 #000000"
        elif status == "disconnected":
            style["rprompt"] = "bg:#ff0066 #ffffff"
        return Style.from_dict(style)

    def run_cli(self):
        try:
            text = self.prompt_session.prompt(
                self.get_prompt_message(),
                style=self.get_style(),
                rprompt=self.get_rprompt,
                auto_suggest=AutoSuggestFromHistory(),
            )
            if not text.strip():
                return
            tokens = safe_split(text) if text else [""]
            command, params, _ = split_command_and_args(tokens)
            self.runner.execute(command, params)
        except KeyboardInterrupt:
            self.runner.stop()
            return

    def terminate(self):
        self.runner.terminate()
