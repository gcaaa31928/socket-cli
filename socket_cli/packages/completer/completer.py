from prompt_toolkit.completion import Completer, Completion
from ..utils.token import safe_split, last_token, get_tokens, split_command_and_args
from ..utils.find_matches import find_collection_matches


class PromptCompleter(Completer):
    def __init__(self, fuzzy, commands, command_opts):
        super().__init__()
        self.commands = commands
        self.command_opts = command_opts
        self.fuzzy = fuzzy

    def find_matches(self, text, collection, fuzzy):
        text = last_token(text).lower()

        for suggestion in find_collection_matches(text, collection, fuzzy):
            yield suggestion

    def find_command_matches(self, command, word, command_opts, fuzzy=False):
        opts = []
        if command in self.command_opts:
            opts = [
                opt
                for opt in self.command_opts[command]
                if opt.name not in command_opts
            ]
        for suggestion in find_collection_matches(word, opts, fuzzy):
            yield suggestion

    def get_completions(self, document, complete_event, smart_completion=None):
        completions = []
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        words = get_tokens(document.text)
        command_name, _, command_opts = split_command_and_args(words)
        in_command = (len(words) > 1) or ((not word_before_cursor) and command_name)
        if in_command:
            return self.find_command_matches(
                command_name, word_before_cursor, command_opts
            )

        return self.find_matches(word_before_cursor, self.commands, self.fuzzy)
