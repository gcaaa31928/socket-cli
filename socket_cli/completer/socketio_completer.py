from prompt_toolkit.completion import Completer, Completion
from collections import namedtuple
from ..utils.token import safe_split, last_token, get_tokens, split_command_and_args
from ..utils.find_matches import find_collection_matches
from ..logger import get_logger
from ..options.socket_option import COMMANDS, COMMAND_OPTS, COMMAND_LENGTH

logger = get_logger()

class SocketIOCompleter(Completer):

    def __init__(self, fuzzy=True):
        super(self.__class__, self).__init__()
        self.fuzzy = fuzzy

    def find_matches(self, text, collection, fuzzy):
        text = last_token(text).lower()

        for suggestion in find_collection_matches(text, collection, fuzzy):
            yield suggestion

    def find_command_matches(self, command, word, command_opts, fuzzy=False):
        opts = []
        if command in COMMAND_OPTS:
            opts = [ opt.arg_name for opt in COMMAND_OPTS[command] if opt.arg_name not in command_opts ]
        for suggestion in find_collection_matches(word, opts, fuzzy):
            yield suggestion

    def get_completions(self, document, complete_event, smart_completion=None):
        completions = []
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        words = get_tokens(document.text)
        command_name, _, command_opts = split_command_and_args(words, COMMAND_LENGTH)
        in_command = (len(words) > 1) or ((not word_before_cursor) and command_name)
        if in_command:
            return self.find_command_matches(command_name, word_before_cursor, command_opts)

        return self.find_matches(word_before_cursor, COMMANDS, self.fuzzy)

