import MySQLdb


# Class for database controlling
class DBController:
    database_name = None
    password = None
    username = None
    connection = None
    cursor = None

    # Constructor for initial all fields and connect to database
    def __init__(self, database_name, password, username):
        self.database_name = database_name
        self.password = password
        self.username = username
        url = 'localhost'
        self.connection = MySQLdb.connect(url, self.username, self.password, self.database_name)
        self.cursor = self.connection.cursor()

    # Method for close database
    def close_db(self):
        self.connection.close()

    # Method for add new section
    def add_section(self, id_se, name):
        try:
            sql = 'INSERT INTO SECTIONS (ID_SE, NAME) VALUES (%d, "%s")' % (id_se, name)
            self.cursor.execute(sql)
            self.connection.commit()
            message = "Section %s Successfully added!" % name
            print(message)
            return message
        except MySQLdb.MySQLError as e:
            print(e)
            self.connection.rollback()
            return e
        except TypeError as t:
            return t

    # Method for add new goods
    def add_goods(self, id_go, id_se, name, price, goods_type):
        try:
            sql = 'INSERT INTO GOODS (ID_GO, ID_SE, NAME, PRICE, GOODSTYPE) VALUES (%d, %d,"%s", %f, "%s")' \
                  % (id_go, id_se, name, price, goods_type)
            self.cursor.execute(sql)
            self.connection.commit()
            message = "Goods %s Successfully added!" % name
            print(message)
            return message
        except MySQLdb.MySQLError as m:
            self.connection.rollback()
            return m
        except TypeError as t:
            return t

    # Method for delete section
    def delete_sections(self, id_se):
        try:
            sql = 'DELETE FROM SECTIONS WHERE ID_SE = %d' % id_se
            self.cursor.execute(sql)
            self.connection.commit()
            message = 'Section with id %d successfully deleted' % id_se
            print(message)
            return message
        except MySQLdb.MySQLError as e:
            self.connection.rollback()
            return e
        except TypeError as t:
            return t

    # Method for delete goods
    def delete_goods(self, id_go):
        try:
            sql = 'DELETE FROM GOODS WHERE ID_GO = %d' % id_go
            self.cursor.execute(sql)
            self.connection.commit()
            message = 'Goods with id %d successfully deleted' % id_go
            print(message)
            return message
        except MySQLdb.MySQLError as e:
            self.connection.rollback()
            return e
        except TypeError as t:
            return t

    # Method for edit section
    def edit_section(self, id_se, parameter, new_data):
        try:
            if parameter == 1:
                sql_sections = 'UPDATE SECTIONS SET ID_SE = %d WHERE ID_SE = %d ' % (new_data, id_se)
            elif parameter == 2:
                sql_sections = 'UPDATE SECTIONS SET NAME = %s WHERE ID_SE = %d' % (new_data, id_se)
            else:
                print('Incorrect parameter!')
            self.cursor.execute(sql_sections)
            self.connection.commit()
            message = 'Section with id %d updated' % id_se
            print(message)
            return message
        except MySQLdb.MySQLError as e:
            self.connection.rollback()
            return e
        except TypeError as t:
            return t

    # Method for edit goods
    def edit_goods(self, id_go, parameter, new_data):
        try:
            if parameter == 1:
                sql = 'UPDATE GOODS SET ID_GO = %d WHERE ID_GO = %d' % (new_data, id_go)
            elif parameter == 2:
                sql = 'UPDATE GOODS SET NAME = %s WHERE ID_GO = %d' % (new_data, id_go)
            elif parameter == 3:
                sql = 'UPDATE GOODS SET PRICE = %f WHERE ID_GO = %d' % (new_data, id_go)
            elif parameter == 4:
                sql = 'UPDATE GOODS SET GOODSTYPE = %s WHERE ID_GO = %d' % (new_data, id_go)
            elif parameter == 5:
                sql = 'UPDATE GOODS SET ID_SE = %d WHERE ID_GO = %d' % (new_data, id_go)
            else:
                print('Incorrect parameter!')
            self.cursor.execute(sql)
            self.connection.commit()
            message = 'Goods with id %d updated' % id_go
            print(message)
            return message
        except MySQLdb.MySQLError as e:
            self.connection.rollback()
            return e
        except TypeError as t:
            return t

    # Method for print goods
    def print_goods(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                id_go = row[0]
                name = row[2]
                price = row[3]
                goods_type = row[4]
                print('%d\t%s\t%f\t%s' % (id_go, name, price, goods_type))
            return results
        except MySQLdb.MySQLError as e:
            self.connection.rollback()
            return e

    # Method for print sections
    def print_sections(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                id_se = row[0]
                name = row[1]
                print('%d\t%s' % (id_se, name))
            return results
        except MySQLdb.MySQLError as e:
            self.connection.rollback()
            return e

    # Method for get section by id
    def get_section(self, id_se):
        try:
            sql = 'SELECT * FROM SECTIONS WHERE ID_SE=%d' % id_se
            return self.print_sections(sql)
        except TypeError as t:
            return t

    # Method for get goods by id
    def get_goods(self, id_go):
        try:
            sql = 'SELECT * FROM GOODS WHERE ID_GO=%d' % id_go
            return self.print_goods(sql)
        except TypeError as t:
            return t

    # Method for get goods by name
    def get_goods_by_name(self, name):
        try:
            sql = 'SELECT * FROM GOODS WHERE NAME ="%s"' % name
            return self.print_goods(sql)
        except TypeError as t:
            return t

    # Method for get all sections
    def get_all_sections(self):
        try:
            sql = 'SELECT * FROM SECTIONS'
            return self.print_sections(sql)
        except TypeError as t:
            return t

    # Method for get all goods
    def get_all_goods(self):
        try:
            sql = 'SELECT * FROM GOODS'
            return self.print_goods(sql)
        except TypeError as t:
            return t

    # Method for get all goods by section id
    def get_all_goods_by_section(self, id_se):
        try:
            sql = 'SELECT * FROM GOODS INNER JOIN SECTIONS ON GOODS.ID_SE = SECTIONS.ID_SE AND SECTIONS.ID_SE = %d' % id_se
            return self.print_goods(sql)
        except TypeError as t:
            return t

    # Method for count goods by section id
    def count_goods_by_sections(self, id_se):
        try:
            sql = 'SELECT COUNT(*) FROM GOODS WHERE ID_SE=%d' % id_se
            results = self.cursor.execute(sql)
            results = self.cursor.fetchone()
            return results[0]
        except MySQLdb.MySQLError as e:
            self.connection.rollback()
            return e
        except TypeError as t:
            return t
