import pickle
import socket
import sys

import storage_sql


class Server:
    server = None
    client = None
    host = None
    port = None
    database = None
    client_data = []

    def __init__(self, port):
        try:
            print("Server is Listening.....")
            self.server = socket.socket()
            self.host = socket.gethostname()
            self.port = port
            self.server.bind((self.host, self.port))
            self.server.listen(5)
            self.client, address = self.server.accept()
            print('Connected by', address)
        except socket.error as e:
            print(e)

    def start(self):
        self.database = storage_sql.DBController('storage', '0961533469Vi', 'root')
        try:
            self.client_data = self.client.recv(4096)
            deserialize_data = pickle.loads(self.client_data)
            operation = int(deserialize_data[0])
            if operation == 0:
                self.add_section(deserialize_data)
            elif operation == 1:
                self.delete_section(deserialize_data)
            elif operation == 2:
                self.add_goods(deserialize_data)
            elif operation == 3:
                self.delete_goods(deserialize_data)
            elif operation == 4:
                self.edit_goods(deserialize_data)
            elif operation == 5:
                self.get_goods_by_name(deserialize_data)
            elif operation == 6:
                self.count_goods_by_sections(deserialize_data)
            elif operation == 7:
                self.get_all_sections()
            elif operation == 8:
                self.get_all_goods_by_section(deserialize_data)
            return True
        except socket.error as s:
            print(s)
            serialize_data = pickle.dumps(s)
            self.client.send(serialize_data)
            return s
        except pickle.PickleError as p:
            print(p)
            serialize_data = pickle.dumps(p)
            self.client.send(serialize_data)
            return p
        except:
            return False

    def add_section(self, deserialize_data):
        data = self.database.add_section(deserialize_data[1], deserialize_data[2])
        serialize_data = pickle.dumps(data)
        self.client.send(serialize_data)

    def delete_section(self, deserialize_data):
        data = self.database.delete_sections(deserialize_data[1])
        serialize_data = pickle.dumps(data)
        self.client.send(serialize_data)

    def add_goods(self, deserialize_data):
        data = self.database.add_goods(deserialize_data[1], deserialize_data[2], deserialize_data[3],
                                       deserialize_data[4], deserialize_data[5])
        serialize_data = pickle.dumps(data)
        self.client.send(serialize_data)

    def delete_goods(self, deserialize_data):
        data = self.database.delete_goods(deserialize_data[1])
        serialize_data = pickle.dumps(data)
        self.client.send(serialize_data)

    def edit_goods(self, deserialize_data):
        data = self.database.edit_goods(deserialize_data[1], deserialize_data[2], deserialize_data[3])
        serialize_data = pickle.dumps(data)
        self.client.send(serialize_data)

    def get_goods_by_name(self, deserialize_data):
        data = self.database.get_goods_by_name(deserialize_data[1])
        serialize_data = pickle.dumps(data)
        self.client.send(serialize_data)

    def count_goods_by_sections(self, deserialize_data):
        data = self.database.count_goods_by_sections(deserialize_data[1])
        serialize_data = pickle.dumps(data)
        self.client.send(serialize_data)

    def get_all_sections(self):
        data = self.database.get_all_sections()
        serialize_data = pickle.dumps(data)
        self.client.send(serialize_data)

    def get_all_goods_by_section(self, deserialize_data):
        data = self.database.get_all_goods_by_section(deserialize_data[1])
        serialize_data = pickle.dumps(data)
        self.client.send(serialize_data)


my_server = Server(12345)
while my_server.start():
    pass
