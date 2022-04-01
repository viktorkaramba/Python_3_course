import socket
import pickle


class Client:
    server = None
    host = None
    port = None
    buffer = None
    client_data = []

    def __init__(self, port):
        self.server = socket.socket()
        self.host = socket.gethostname()
        self.port = port

    # Method for connect to server
    def connect(self):
        self.server.connect((self.host, self.port))

    # Method for close sever
    def close(self):
        self.server.close()

    # Method for send query
    def send_query(self):
        try:
            serialize_data = pickle.dumps(self.client_data)
            self.server.send(serialize_data)
            data = self.server.recv(4096)
            deserialize_data = pickle.loads(data)
            self.client_data.clear()
            return deserialize_data
        except pickle.PickleError as p:
            print(p)
            return p
        except socket.error as s:
            print(s)
            return s

    # Method for add section
    def add_section(self, id_se, name):
        self.client_data.append(0)
        self.client_data.append(id_se)
        self.client_data.append(name)
        return self.send_query()

    # Method for delete section
    def delete_section(self, id_se):
        self.client_data.append(1)
        self.client_data.append(id_se)
        return self.send_query()

    # Method for add goods
    def add_goods(self, id_go, id_se, name, price, goods_type):
        self.client_data.append(2)
        self.client_data.append(id_go)
        self.client_data.append(id_se)
        self.client_data.append(name)
        self.client_data.append(price)
        self.client_data.append(goods_type)
        return self.send_query()

    # Method for delete goods
    def delete_goods(self, id_go):
        self.client_data.append(3)
        self.client_data.append(id_go)
        return self.send_query()

    # Method for edit goods
    def edit_goods(self, id_go, parameter, new_data):
        self.client_data.append(4)
        self.client_data.append(id_go)
        self.client_data.append(parameter)
        self.client_data.append(new_data)
        return self.send_query()

    # Method for get goods by name
    def get_goods_by_name(self, name):
        self.client_data.append(5)
        self.client_data.append(name)
        return self.send_query()

    # Method for count goods by section
    def count_goods_by_section(self, id_se):
        self.client_data.append(6)
        self.client_data.append(id_se)
        return self.send_query()

    # Method for get all sections
    def get_all_sections(self):
        self.client_data.append(7)
        return self.send_query()

    # Method for get all goods by section
    def get_all_goods_by_section(self, id_se):
        self.client_data.append(8)
        self.client_data.append(id_se)
        return self.send_query()


client = Client(12345)
client.connect()
print(client.add_section(4, 'Sport equipment'))
print(client.get_all_sections())
print(client.add_goods(7, 4, 'Net', 499.99, 'Football'))
print(client.get_all_goods_by_section(1))
print(client.get_goods_by_name('Net'))
print(client.edit_goods(7, 1, 8))
print(client.get_all_goods_by_section(4))
print(client.add_goods(7, 1, 'Orange', 2.99, 'Fruits'))
print(client.get_all_goods_by_section(1))
print(client.count_goods_by_section(1))
print(client.delete_goods(7))
print(client.delete_section(4))
print(client.get_all_sections())
print(client.get_all_goods_by_section(4))
client.close()
