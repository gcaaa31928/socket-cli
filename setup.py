from socket_cli.__init__ import __version__
import sys, subprocess

try:
    from setuptools import setup, find_packages, Command
except ImportError:
    from distutils.core import setup

install_requirements = [
    "click>=4.0",
    "prompt_toolkit>=2.0.10",
    "fuzzyfinder>=2.1.0",
    "python-socketio>=4.3.1",
    "pygments>=2.4.2",
    "halo",
    "websockets>=8.1",
    "asyncio>=3.4.3",
    "requests",
]


class lint(Command):
    description = "check code use black (and fix violations)"

    user_options = [("fix", "f", "fix the violations in place")]

    def initialize_options(self):
        self.fix = False

    def finalize_options(self):
        pass

    def run(self):
        cmd = "black"
        if not self.fix:
            cmd += " --check"
        cmd += " ."
        sys.exit(subprocess.call(cmd, shell=True))


setup(
    name="socket-cli",
    version=__version__,
    author="gcaaa31928",
    author_email="gcaaa31928@gmail.com",
    packages=find_packages(),
    description="CLI for SocketIO, WebSocket, Unix-Socket. With auto-completion and syntax highlighting.",
    entry_points={"console_scripts": ["socket-cli = socket_cli.main:cli"],},
    cmdclass={"lint": lint},
    url="http://pypi.python.org/pypi/PackageName/",
    license="LICENSE.txt",
    long_description=open("README.md").read(),
    install_requires=install_requirements,
    classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "Operating System :: Unix",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
