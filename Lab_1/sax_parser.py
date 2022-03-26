import xml.sax
from storage.goods import Goods
from storage.section import Section
from storage.storage import Storage


class StorageHandler(xml.sax.handler.ContentHandler):
    current_data = None
    section = Section()
    goods = Goods()
    is_goods = False
    storage = Storage()

    def startElement(self, name, attrs):
        self.current_data = name
        if name == "Section":
            self.section.set_id(attrs["id"])
            self.section.set_name(attrs["name"])
            self.storage.add_section(self.section.id, self.section.name)
        elif name == "Goods":
            self.goods.set_id(attrs["id"])
            self.goods.set_name(attrs["name"])
            self.goods.set_price(attrs["price"])
            self.goods.set_section_code(self.section.id)
            self.goods.set_goods_type(attrs["goods_type"])
            self.storage.add_goods(self.goods.id, self.goods.name,
                                   self.goods.price, self.section.id, self.goods.goods_type)