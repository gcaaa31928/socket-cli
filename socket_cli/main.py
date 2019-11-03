from __future__ import print_function
from __future__ import unicode_literals

import click
import traceback
from urllib.parse import urlparse
from .packages.prompt.socketio_prompt import SocketIOPrompt
from .packages.prompt.websocket_prompt import WebSocketPrompt
from .packages.prompt.unix_socket_prompt import UnixSocketPrompt
from .packages.commands.command import argparse
from .packages.logger import get_logger


logger = get_logger()

@click.argument('path', default='', nargs=1)
@click.command()
def cli(path):
    url = urlparse(path)
    if url.scheme == 'http':
        prompt = SocketIOPrompt(path)
    elif url.scheme == 'ws':
        prompt = WebSocketPrompt(path)
    else:
        prompt = UnixSocketPrompt(path)
    while True:
        try:
            prompt.run_cli()
        except argparse.ArgumentError as ex:
            self.logger.debug('Error: %r.', ex)
            self.logger.error("traceback: %r", traceback.format_exc())
            click.secho(ex.msg, fg='red')

        except EOFError:
            # exit out of the CLI
            prompt.terminate()
            break

        except Exception as ex:
            logger.debug('Exception: %r.', ex)
            logger.error("traceback: %r", traceback.format_exc())
            click.secho(str(ex), fg='red')

if __name__ == "__main__":
    cli()
