from xml.dom import minidom
from storage.goods import Goods
from storage.section import Section
import exceptions


class Storage:
    sections = []
    goods = []

    def get_section(self, id):
        for section in self.sections:
            if section.id == id:
                return section
        raise exceptions.NonSectionError

    def get_section_ind(self, ind):
        for i in range(len(self.sections)):
            if i == ind:
                return self.sections[i]
        raise exceptions.MyIndexError

    def get_goods(self, id):
        for goods in self.goods:
            if goods.id == id:
                return goods
        raise exceptions.NonGoodsError

    def get_goods_ind(self, ind):
        for i in range(len(self.goods)):
            if i == ind:
                return self.goods[i]
        raise exceptions.MyIndexError

    def count_sections(self):
        return len(self.sections)

    def add_section(self, id, name):
        for section in self.sections:
            if section.id == id:
                raise exceptions.AlreadySectionError
        self.sections.append(Section(id, name))

    def add_goods(self, id, name, price, section_code, goods_type):
        is_section = False
        for section in self.sections:
            if section.id == section_code:
                is_section = True
                for goods in self.goods:
                    if goods.id == id:
                        raise exceptions.AlreadyGoodsError
        if is_section:
            self.goods.append(Goods(id, name, price, section_code, goods_type))
        else:
            raise exceptions.NonSectionError

    def delete_section(self, id):
        is_section = False
        is_goods = False
        for section in self.sections:
            if section.id == id:
                is_section = True
                self.sections.remove(section)
                for goods in self.goods:
                    if goods.section_code == id:
                        is_goods = True
                        print(goods.id, goods.name)
                        self.goods.remove(goods)
                        break
                break
        if not is_section:
            raise exceptions.NonSectionError
        elif not is_goods:
            raise exceptions.NonGoodsError

    def delete_goods(self, id):
        is_goods = False
        for goods in self.goods:
            if goods.id == id:
                is_goods = True
                self.goods.remove(goods)
                break
        if not is_goods:
            raise exceptions.NonGoodsError

    def edit_section(self, id, parameter, new_data):
        is_section = False
        for section in self.sections:
            if section.id == id:
                is_section = True
                old_id = section.id
                if parameter == 1:
                    section.id = new_data
                    for goods in self.goods:
                        if goods.section_code == old_id:
                            goods.section_code = new_data
                elif parameter == 2:
                    section.name = new_data
                else:
                    raise exceptions.InputError('Error input: please choose parameters between 1 and 2')
        if not is_section:
            raise exceptions.NonSectionError

    def edit_goods(self, id, parameter, new_data):
        is_goods = False
        for goods in self.goods:
            if goods.id == id:
                is_goods = True
                if parameter == 1:
                    goods.id = new_data
                elif parameter == 2:
                    goods.name = new_data
                elif parameter == 3:
                    goods.price = new_data
                elif parameter == 4:
                    goods.goods_type = new_data
                else:
                    raise exceptions.InputError('Error input: please choose parameters between 1 and 4')
        if not is_goods:
            raise exceptions.NonGoodsError

    def save_to_file(self, filename):
        root = minidom.Document()
        xml = root.createElement('Storage')
        xml.setAttribute('xmlns', 'http://viktorkaramba.com.Lab_1/storage')
        xml.setAttribute('xmlns:xsd', 'http://www.w3.org/2001/XMLSchema-instance')
        xml.setAttribute('xsd:schemaLocation', 'http://viktorkarmba.com.Lab_1/storage storage.xsd')
        root.appendChild(xml)
        for i in range(len(self.sections)):
            section_ = root.createElement('Section')
            section_.setAttribute('id', self.sections[i].id)
            section_.setAttribute('name', self.sections[i].name)
            sub_root = xml.appendChild(section_)
            for j in range(len(self.goods)):
                if self.goods[j].section_code == self.sections[i].id:
                    goods_ = root.createElement('Goods')
                    goods_.setAttribute('id', self.goods[j].id)
                    goods_.setAttribute('name', self.goods[j].name)
                    goods_.setAttribute('price', self.goods[j].price)
                    goods_.setAttribute('goods_type', self.goods[j].goods_type)
                    sub_root.appendChild(goods_)

        xml_str = root.toprettyxml(indent='\t')
        save_path_file = filename
        with open(save_path_file, 'w') as f:
            f.write(xml_str)

    def get_all_list_sections(self):
        for section in self.sections:
            print('id:', section.id, ', name:', section.name)

    def get_all_list_goods(self, section_code):
        is_section = False
        for section in self.sections:
            if section.id == section_code:
                is_section = True
                for goods in self.goods:
                    if goods.section_code == section_code:
                        print('id:', goods.id, ', name:', goods.name,
                              ', price:', goods.price, ', goods type:', goods.goods_type)
        if not is_section:
            raise exceptions.NonSectionError
