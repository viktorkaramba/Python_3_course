import pickle
import storage_sql
import pika, sys, os
import config


class Server:
    client_data = []
    channel = None
    database = None

    def __init__(self):
        self.database = storage_sql.DBController(config.database_name, config.password, config.username)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = connection.channel()
        self.channel.basic_consume(queue='TO.SERV', auto_ack=True, on_message_callback=self.callback)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        try:
            self.client_data = pickle.loads(body)
            print(" [x] Received ", int(self.client_data[0]))
            operation = int(self.client_data[0])
            if operation == 0:
                self.add_section(ch, properties)
            elif operation == 1:
                self.delete_section(ch, properties)
            elif operation == 2:
                self.add_goods(ch, properties)
            elif operation == 3:
                self.delete_goods(ch, properties)
            elif operation == 4:
                self.edit_goods(ch, properties)
            elif operation == 5:
                self.get_goods_by_name(ch, properties)
            elif operation == 6:
                self.count_goods_by_sections(ch, properties)
            elif operation == 7:
                self.get_all_sections(ch, properties)
            elif operation == 8:
                self.get_all_goods_by_section(ch, properties)
            else:
                self.reply(ch, properties, 'Incorrect operation')
            self.client_data.clear()
            return True
        except pickle.PickleError as p:
            self.reply(ch, properties, p)
        except:
            return False

    def reply(self, ch, properties, response):
        ch.basic_publish(exchange='',
                         routing_key=properties.reply_to,
                         body=response,
                         properties=pika.BasicProperties(
                             delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                         ))

    def add_section(self, ch, properties):
        data = self.database.add_section(self.client_data[1], self.client_data[2])
        serialize_data = pickle.dumps(data)
        self.reply(ch, properties, serialize_data)

    def delete_section(self, ch, properties):
        data = self.database.delete_sections(self.client_data[1])
        serialize_data = pickle.dumps(data)
        self.reply(ch, properties, serialize_data)

    def add_goods(self, ch, properties):
        data = self.database.add_goods(self.client_data[1], self.client_data[2], self.client_data[3],
                                       self.client_data[4], self.client_data[5])
        serialize_data = pickle.dumps(data)
        self.reply(ch, properties, serialize_data)

    def delete_goods(self, ch, properties):
        data = self.database.delete_goods(self.client_data[1])
        serialize_data = pickle.dumps(data)
        self.reply(ch, properties, serialize_data)

    def edit_goods(self, ch, properties):
        data = self.database.edit_goods(self.client_data[1], self.client_data[2], self.client_data[3])
        serialize_data = pickle.dumps(data)
        self.reply(ch, properties, serialize_data)

    def get_goods_by_name(self, ch, properties):
        data = self.database.get_goods_by_name(self.client_data[1])
        serialize_data = pickle.dumps(data)
        self.reply(ch, properties, serialize_data)

    def count_goods_by_sections(self, ch, properties):
        data = self.database.count_goods_by_sections(self.client_data[1])
        serialize_data = pickle.dumps(data)
        self.reply(ch, properties, serialize_data)

    def get_all_sections(self, ch, properties):
        data = self.database.get_all_sections()
        serialize_data = pickle.dumps(data)
        self.reply(ch, properties, serialize_data)

    def get_all_goods_by_section(self, ch, properties):
        data = self.database.get_all_goods_by_section(self.client_data[1])
        serialize_data = pickle.dumps(data)
        self.reply(ch, properties, serialize_data)


if __name__ == '__main__':
    try:
        server = Server()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


# def processQuery():
#     try:
#         oper = getq.get(gmo)
#         v1 = getq.get(gmo)
#         v2 = getq.get(gmo)
#         response = v1 + v2 if (oper == 0) else v1 - v2
#         putq.put(oper)
#         putq.put(v1)
#         putq.put(v2)
#         putq.put(response)
#         return True
#     except:
#         return False
#
#
# i = 0
# while (processQuery()):
#     i += 1
# print("Опрацьовано" + i + "Запитів")