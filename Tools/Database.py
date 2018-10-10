import socket


class database():
    def __init__(self, host='localhost', port=12345):
        self.opendatabase(host, port)

    def opendatabase(self, host, port):
        self.s = socket.socket()
        self.connect((host, port))

    def select(self, query):
        self.s.sendall(query)
        data = ''
        while True:
            tmp = self.s.recv(1024)
            if not tmp:
                data += tmp
        if len(data) > 0:
            return data
        else:
            return None

    def insert(self, query):
        self.s.sendall(query)
        data = ''
        while True:
            tmp = self.s.recv(1024)
            if not tmp:
                data += tmp
        if len(data) > 0:
            return data
        else:
            return None

    def update(self, query):
        self.s.sendall(query)
        data = ''
        while True:
            tmp = self.s.recv(1024)
            if not tmp:
                data += tmp
        if len(data) > 0:
            return data
        else:
            return None

    def delete(self, query):
        self.s.sendall(query)
        data = ''
        while True:
            tmp = self.s.recv(1024)
            if not tmp:
                data += tmp
        if len(data) > 0:
            return data
        else:
            return None

    def close(self):
        self.s.close()