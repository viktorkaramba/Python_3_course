class Goods:
    id = None
    name = None
    price = None
    section_code = None
    goods_type = None

    def __init__(self, id=None, name=None, price=None, section_code=None, goods_type=None):
        self.id = id
        self.name = name
        self.price = price
        self.section_code = section_code
        self.goods_type = goods_type

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_section_code(self, section_code):
        self.section_code = section_code

    def set_goods_type(self, goods_type):
        self.goods_type = goods_type
