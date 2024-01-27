import socket
from io import StringIO


def parse_http(http):
    request, *headers, _, body = http.split("\r\n")
    method, path, protocol = request.split(" ")
    headers = dict(line.split(": ", maxsplit=1) for line in headers)
    return method, path, protocol, headers, body


def process_response(response):
    print("Calling process_response")
    return (
        "HTTP/1.1 200 OK\r\n"
        f"Content-Length: {len(response)}\r\n"
        "Content-Type: text/html\r\n"
        "\r\n"
        f"{response}"
        "\r\n"
    )


def format_headers(headers):
    return {
        "HTTP_" + key.upper().replace("-", "_"): value for key, value in headers.items()
    }


def start_response(status, headers):
    conn.sendall(f"HTTP/1.1 {status}\r\n".encode("utf-8"))
    for key, value in headers:
        conn.sendall(f"{key}: {value}\r\n".encode("utf-8"))
    conn.sendall(b"\r\n")


# make request wgsi compatible
def to_environ(method, path, protocol, headers, body):
    return {
        "REQUEST_METHOD": method,
        "PATH_INFO": path,
        "SERVER_PROTOCOL": protocol,
        "wsgi.input": StringIO(body),
        **format_headers(headers),
    }


def view(environ):
    return f"Hello World! {environ['PATH_INFO']}"


def application(environ, start_response):
    response = view(environ)
    start_response("200 OK", [("Content-Type", "text/html")])
    return [response.encode("utf-8")]


# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     print("Calling this code gunicorn")
#     s.bind(("localhost", 8000))
#     s.listen(1)

#     while True:
#         conn, addr = s.accept()
#         with conn:
#             print("Connected by", addr)
#             request = conn.recv(1024)
#             if not request:
#                 break
#             request = request.decode("utf-8")
#             request = parse_http(request)
#             environ = to_environ(*request)
#             response = application(environ, start_response)
#             for data in response:
#                 print(data)
#                 conn.sendall(data)