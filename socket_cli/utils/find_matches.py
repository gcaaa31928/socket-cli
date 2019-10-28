from prompt_toolkit.completion import Completion
import fuzzyfinder

def find_collection_matches(word, lst, fuzzy):
    if lst is None:
        return []
    if fuzzy:
        for suggestion in fuzzyfinder.fuzzyfinder(word, lst):
            yield Completion(suggestion, -len(word), display_meta=suggestion)
    else:
        for name in sorted(lst):
            if name.startswith(word) or not word:
                yield Completion(name, -len(word), display_meta=name)
