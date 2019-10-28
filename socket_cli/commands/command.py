import argparse

class Command(object):
    def __init__(self):
        pass

    def parse_command_options(self, command_list, params):
        if command_list is None:
            return None

        self.parser = argparse.ArgumentParser()
        for opt in command_list.get_all_options():
            self.parser.add_argument(*opt['argv'], **opt['kwargs'], nargs='?')
        return self.parser.parse_args(params)

