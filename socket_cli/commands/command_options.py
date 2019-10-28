class CommandList(object):
    def __init__(self, arr):
        self.arr = arr

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.arr):
            raise StopIteration
        else:
            obj = self.arr[self.index]
            self.index += 1
            return obj

    def get_all_options(self):
        for option in self.arr:
            argv = ['--' + option.name]
            kwargs = {
                #'type': option.type,
                'default': option.default
            }
            yield { 'argv': argv, 'kwargs': kwargs }

class CommandOption(object):
    def __init__(self, name, type, default=None):
        self.name = name
        self.type = type
        self.default = default

    @property
    def arg_name(self):
        return '--' + self.name
