import Pyro4
import config

from storage_db import DBController

deamon = Pyro4.Daemon()
uri = deamon.register(DBController(config.database_name, config.password, config.username))
ns = Pyro4.locateNS()
ns.register('storage_db', uri)
deamon.requestLoop()
