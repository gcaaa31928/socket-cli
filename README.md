<h1 align="center">Welcome to socket-cli 👋</h1>
<p align="center">
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/socket-cli">
  <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/socket-cli?style=flat-square">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/socket-cli">
</p>

> A command-line client for socket.io, websocket, unix-socket that has auto-completion and syntax highlighting.

## ✨ Demo

### Just take a look
[![asciicast](https://asciinema.org/a/GgXCsrUEhlY98xxlrhIQcRpNj.svg)](https://asciinema.org/a/GgXCsrUEhlY98xxlrhIQcRpNj?speed=2)

## 🚀 Usage

install *socket-cli* via pip:

```bash
pip install socket-cli
```
```bash
Usage: socket-cli [OPTIONS] [PATH]

Options:
  -t, --type TEXT  [websocket, socketio, unix]
  --help           Show this message and exit.
````

when you connect a socket.io server.
```bash
> connect
> emit --event event_name --data '{"test": "data"}'
> on --event event_name
> on --event event_name --namespace /admin
> emit --event event_name --data '{"test": "data"}' --namespace /admin
```
or a websocket server
```bash
> connect
> send --data test
> recv 
```
or a unix socket server
```bash
> connect
> send --data test
```

```bash
> connect
> send --data 
> on --event event_name
```

## 🤝 Contributing

Contributions, issues and feature requests are welcome.<br />
Feel free to check [issues page](https://github.com/gcaaa31928/socket-cli/issues) and pull-request welcome.


## TODO
- [ ] connect socket.io server with headers
- [ ] unit-testing, ci


## Author

👤 **gcaaa31928**

* Website: http://gcaaa.blogspot.tw/
* Github: [@gcaaa31928](https://github.com/gcaaa31928)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
