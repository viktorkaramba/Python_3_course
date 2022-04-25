import pickle
import uuid

import pika


class Client:
    client_data = []
    connection = None
    channel = None

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    def send_query(self):
        self.channel = self.connection.channel()
        self.channel.basic_consume(queue='TO.CL', auto_ack=True, on_message_callback=self.callback)
        serialize = pickle.dumps(self.client_data)
        self.client_data.clear()
        cor_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='TO.SERV',
                                   body=serialize,
                                   properties=pika.BasicProperties(
                                       delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE,
                                       reply_to='TO.CL',
                                       correlation_id=cor_id,
                                   ))
        print(" [x] Sent data")
        self.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        result = pickle.loads(body)
        print(" [x] Answer ", result)
        self.channel.close()

    def close(self):
        self.channel.close()

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


client = Client()
client.add_section(4, 'Sport equipment')
client.get_all_sections()
print('#'*50)
client.add_goods(17, 4, 'Net', 499.99, 'Football')
client.get_all_goods_by_section(1)
print('#'*50)
client.get_goods_by_name('Net')
client.edit_goods(17, 1, 9)
client.get_all_goods_by_section(4)
print('#'*50)
client.add_goods(10, 1, 'Samsung Galaxy A71', 299.99, 'smartphone')
client.get_all_goods_by_section(1)
print('#'*50)
client.count_goods_by_section(1)
print('#'*50)
client.delete_goods(10)
client.get_all_goods_by_section(1)
print('#'*50)
client.delete_section(4)
client.get_all_sections()
print('#'*50)
client.get_all_goods_by_section(4)
