from ..commands.command_options import CommandList, CommandOption

COMMAND_OPTS = {
    "send": CommandList([CommandOption("--data", "string", desc="data payload"),]),
    "recv": CommandList([]),
}

COMMANDS = [
    CommandOption("connect", desc="connect to websocket server"),
    CommandOption("send", desc="send data"),
    CommandOption("recv", desc="receive data"),
]
