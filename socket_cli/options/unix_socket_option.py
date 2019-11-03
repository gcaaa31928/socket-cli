from ..commands.command_options import CommandList, CommandOption

COMMAND_OPTS = {
    'send': CommandList([
        CommandOption('data', 'string'),
    ]),
    'recv': CommandList([
    ])
}

COMMANDS = [
    'connect',
    'send',
    'recv',
]

COMMAND_LENGTH = dict((k, len(k.split(' '))) for k in COMMANDS if ' ' in k)
