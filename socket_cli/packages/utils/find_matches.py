from prompt_toolkit.completion import Completion
import fuzzyfinder


def find_collection_matches(word, options, fuzzy):
    if options is None:
        return []
    if fuzzy:
        for suggestion in fuzzyfinder.fuzzyfinder(
            word, options, accessor=lambda x: x.name
        ):
            yield Completion(suggestion.name, -len(word), display_meta=suggestion.desc)
    else:
        for option in sorted(options, key=lambda x: x.name):
            if option.name.startswith(word) or not word:
                yield Completion(option.name, -len(word), display_meta=option.desc)
