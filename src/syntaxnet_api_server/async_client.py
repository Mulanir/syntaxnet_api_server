import socket


if __name__ == "__main__":
    socket = socket.create_connection(('localhost', 8111))

    while True:
        message = input()

        socket.send(bytearray(message))
