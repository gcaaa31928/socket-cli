from ..commands.command_options import CommandList, CommandOption

COMMAND_OPTS = {
    'emit': CommandList([
        CommandOption('event', 'string'),
        CommandOption('data', 'string'),
        CommandOption('namespace', 'string', default='/')
    ]),
    'on': CommandList([
        CommandOption('event', 'string'),
        CommandOption('namespace', 'string', default='/')
    ])
}

COMMANDS = [
    'header',
    'connect',
    'disconnect',
    'emit',
    'on',
    'start_receiving',
]

COMMAND_LENGTH = dict((k, len(k.split(' '))) for k in COMMANDS if ' ' in k)
