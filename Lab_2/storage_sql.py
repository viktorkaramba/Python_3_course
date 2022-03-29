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
        sql = 'INSERT INTO SECTIONS (ID_SE, NAME) VALUES (%d, "%s")' % (id_se, name)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Section %s Successfully added!" % name)
            return True
        except MySQLdb.MySQLError as e:
            print(e)
            self.connection.rollback()
            return False

    # Method for add new goods
    def add_goods(self, id_go, id_se, name, price, goods_type):
        sql = 'INSERT INTO GOODS (ID_GO, ID_SE, NAME, PRICE, GOODSTYPE) VALUES (%d, %d,"%s", %f, "%s")' \
              % (id_go, id_se, name, price, goods_type)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Goods %s Successfully added!" % name)
            return True
        except MySQLdb.MySQLError as e:
            print(e)
            self.connection.rollback()
            return False

    # Method for delete section
    def delete_sections(self, id_se):
        sql = 'DELETE FROM SECTIONS WHERE ID_SE = %d' % id_se
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print('Section with id %d successfully deleted' % id_se)
            return True
        except MySQLdb.MySQLError as e:
            print(e)
            self.connection.rollback()
            return False

    # Method for delete goods
    def delete_goods(self, id_go):
        sql = 'DELETE FROM GOODS WHERE ID_GO = %d' % id_go
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print('Goods with id %d successfully deleted' % id_go)
            return True
        except MySQLdb.MySQLError as e:
            print(e)
            self.connection.rollback()
            return False

    # Method for edit section
    def edit_section(self, id_se):
        print('Please select the setting you want to change in section:')
        print('1 - id')
        print('2 - name')
        setting = int(input())
        if setting == 1:
            new_id = int(input('Input new id for section: '))
            sql_sections = 'UPDATE SECTIONS SET ID_SE = %d WHERE ID_SE = %d ' % (new_id, id_se)
        elif setting == 2:
            new_name = input('Input new name for section: ')
            sql_sections = 'UPDATE SECTIONS SET NAME = %s WHERE ID_SE = %d' % (new_name, id_se)
        try:
            self.cursor.execute(sql_sections)
            self.connection.commit()
            print('Section with id %d updated' % id_se)
            return True
        except MySQLdb.MySQLError as e:
            print(e)
            self.connection.rollback()
            return False

    # Method for edit goods
    def edit_goods(self, id_go):
        print('Please select the setting you want to change in goods:')
        print('1 - id')
        print('2 - name')
        print('3 - price')
        print('4 - goods type')
        print('5 - section id')
        setting = int(input())
        if setting == 1:
            new_id = int(input('Input new id for goods: '))
            sql = 'UPDATE GOODS SET ID_GO = %d WHERE ID_GO = %d' % (new_id, id_go)
        elif setting == 2:
            new_name = input('Input new name for goods: ')
            sql = 'UPDATE GOODS SET NAME = %s WHERE ID_GO = %d' % (new_name, id_go)
        elif setting == 3:
            new_price = float(input('Input new price for goods: '))
            sql = 'UPDATE GOODS SET PRICE = %f WHERE ID_GO = %d' % (new_price, id_go)
        elif setting == 4:
            new_goods_type = input('Input new goods type for goods: ')
            sql = 'UPDATE GOODS SET GOODSTYPE = %s WHERE ID_GO = %d' % (new_goods_type, id_go)
        elif setting == 5:
            new_section_id = int(input('Input new section id for goods: '))
            sql = 'UPDATE GOODS SET ID_SE = %d WHERE ID_GO = %d' % (new_section_id, id_go)
        else:
            print('Incorrect data!')
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print('Goods with id %d updated' % id_go)
            return True
        except MySQLdb.MySQLError as e:
            print(e)
            self.connection.rollback()
            return False

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
            return True
        except MySQLdb.MySQLError as e:
            print(e)
            self.connection.rollback()
            return False

    # Method for get section by id
    def get_section(self, id_se):
        sql = 'SELECT * FROM SECTIONS WHERE ID_SE=%d' % id_se
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                id_se = row[0]
                name = row[1]
                print('%d\t%s' % (id_se, name))
            return True
        except MySQLdb.MySQLError as e:
            print(e)
            self.connection.rollback()
            return False

    # Method for get goods by id
    def get_goods(self, id_go):
        sql = 'SELECT * FROM GOODS WHERE ID_GO=%d' % id_go
        self.print_goods(sql)

    # Method for get all sections
    def get_all_sections(self):
        sql = 'SELECT * FROM SECTIONS'
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                id_se = row[0]
                name = row[1]
                print('%d\t%s' % (id_se, name))
            return True
        except MySQLdb.MySQLError as e:
            print(e)
            self.connection.rollback()
            return False

    # Method for get all goods
    def get_all_goods(self):
        sql = 'SELECT * FROM GOODS'
        self.print_goods(sql)

    # Method for get al goods by section id
    def get_all_goods_by_section(self, id_se):
        sql = 'SELECT * FROM GOODS INNER JOIN SECTIONS ON GOODS.ID_SE = SECTIONS.ID_SE AND SECTIONS.ID_SE = %d' % id_se
        self.print_goods(sql)
