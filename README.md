# Fake API

```python
usage: fa.py [-h] [-a ADDR] [-p PORT] [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -a ADDR, --addr ADDR  Serve on this address. Default: 127.0.0.1. Optional.
  -p PORT, --port PORT  Serve on this port. Default: 8080. Optional.
  -f FILE, --file FILE  Use responses from this file.
```

Un ejemplo de JSON *correcto* es el siguiente (es necesario usar doble-comillas):

```
{
    "GET":{
        "/api/hello": {
            "status": 200,
            "body": "Hello world!",
            "headers": {"Content-type": "text/plain"}
        },
        "/api/hello.html": {
            "status": 200,
            "body": "<html><body><h1>Hello World!</h1></body></html>",
            "headers": {"Content-type": "text/html"}
        },
        "/api/hello.json": {
            "status": 200,
            "body": {"message":"Hello World!"},
            "headers": {"Content-type": "application/json"}
        },
    }
}
```

## License

See [LICENSE]
