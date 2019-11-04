from prompt_toolkit.completion import Completion
import shlex


def safe_split(text):
    try:
        words = shlex.split(text)
        return words
    except:
        return [text]


def get_tokens(text):
    if text is not None:
        text = text.strip()
        words = safe_split(text)
        return words
    return []


def last_token(text):
    if text is not None:
        text = text.strip()
        if len(text) > 0:
            word = safe_split(text)[-1]
            word = word.strip()
            return word
    return ""


def find_filepath_matches(word):
    base_path, last_path, position = parse_path(word)
    paths = list_dir(word, dirs_only=False)
    for name in sorted(paths):
        suggestion = complete_path(name, last_path)
        if suggestion:
            yield Completion(suggestion, position)


def find_directory_matches(word):
    base_dir, last_dir, position = parse_path(word)
    dirs = list_dir(word, dirs_only=True)
    for name in sorted(dirs):
        suggestion = complete_path(name, last_dir)
        if suggestion:
            yield Completion(suggestion, position)


def split_command_and_args(tokens):
    command, args = None, None
    if tokens:
        command = tokens[0]
        args = tokens[1:] if len(tokens) >= 1 else None
        opts = []
        for token in tokens[1:]:
            if "--" in token:
                opts.append(token)

    return command, args, opts
