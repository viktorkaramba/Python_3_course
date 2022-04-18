from time import sleep

import Pyro4

ns = Pyro4.locateNS()
uri = ns.lookup('storage_db')
client = Pyro4.Proxy(uri)

sleep(5)
print(client.get_all_sections())
print('#'*50)
sleep(1)
print(client.add_section(5, 'Clothing'))
print(client.get_all_sections())
sleep(1)
print('#'*50)
print(client.add_goods(9, 5, 'T-shirt', 5.99, 'Summer clothes'))
sleep(1)
print('#'*50)
print(client.get_all_goods())
sleep(1)
print('#'*50)
print(client.delete_goods(4))
print(client.get_all_goods())
sleep(1)
print('#'*50)
print(client.edit_goods(11, 1, 7))
print(client.get_goods(7))
