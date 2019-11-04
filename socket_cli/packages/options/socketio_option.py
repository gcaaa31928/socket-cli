from ..commands.command_options import CommandList, CommandOption

COMMAND_OPTS = {
    "emit": CommandList(
        [
            CommandOption("--event", "string", desc="event name"),
            CommandOption("--data", "string", desc="data payload"),
            CommandOption(
                "--namespace",
                "string",
                default="/",
                desc="different endpoints or paths",
            ),
        ]
    ),
    "on": CommandList(
        [
            CommandOption("--event", "string", desc="event name"),
            CommandOption(
                "--namespace",
                "string",
                default="/",
                desc="different endpoints or paths",
            ),
        ]
    ),
    "connect": CommandList(
        [
            CommandOption(
                "--namespace",
                "string",
                default="/",
                desc="different endpoints or paths",
            )
        ]
    ),
}

COMMANDS = [
    CommandOption("connect", desc="connect to socket.io server"),
    CommandOption("emit", desc="emit event"),
    CommandOption("on", desc="receive event"),
]
