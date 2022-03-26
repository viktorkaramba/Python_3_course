from xml.dom import minidom
from storage.goods import Goods
from storage.section import Section
import exceptions


class Storage:
    sections = []
    goods = []

    def get_section(self, id):
        for i in range(len(self.sections)):
            if self.sections[i].id == id:
                return self.sections[i]
        raise exceptions.NonSectionError

    def get_section_ind(self, ind):
        for i in range(len(self.sections)):
            if i == ind:
                return self.sections[i]
        raise exceptions.MyIndexError

    def get_goods(self, id):
        for i in range(len(self.goods)):
            if self.goods[i].id == id:
                return self.goods[i]
        raise exceptions.NonGoodsError

    def get_goods_ind(self, ind):
        for i in range(len(self.goods)):
            if i == ind:
                return self.goods[i]
        raise exceptions.MyIndexError

    def count_sections(self):
        return len(self.sections)

    def add_section(self, id, name):
        for i in range(len(self.sections)):
            if self.sections[i].id == id:
                raise exceptions.AlreadySectionError
        self.sections.append(Section(id, name))

    def add_goods(self, id, name, price, section_code, goods_type):
        section_id = None
        is_section = False
        for i in range(len(self.sections)):
            if self.sections[i].id == section_code:
                section_id = section_code
                is_section = True
                for j in range(len(self.goods)):
                    if self.goods[j].id == id:
                        raise exceptions.AlreadyGoodsError
        if is_section:
            self.goods.append(Goods(id, name, price, section_id, goods_type))
        else:
            raise exceptions.NonSectionError

    def delete_section(self, id):
        is_section = False
        is_goods = False
        for i in range(len(self.sections)):
            if self.sections[i].id == id:
                is_section = True
                self.sections.pop(i)
                print(i)
                for j in range(len(self.goods)):
                    if self.goods[j].section_code == id:
                        is_goods = True
                        print(self.goods[j].id, self.goods[j].name)
                        self.goods.pop(j)
                        break
                break
        if not is_section:
            raise exceptions.NonSectionError
        elif not is_goods:
            raise exceptions.NonGoodsError

    def delete_goods(self, id):
        is_goods = False
        for i in range(len(self.goods)):
            if self.goods[i].id == id:
                is_goods = True
                self.goods.pop(i)
                break
        if not is_goods:
            raise exceptions.NonGoodsError

    def edit_section(self, id):
        print('Please select the setting you want to change in section:')
        print('1 - id')
        print('2 - name')
        setting = int(input())
        is_section = False
        for i in range(len(self.sections)):
            if self.sections[i].id == id:
                is_section = True
                old_id = self.sections[i].id
                if setting == 1:
                    new_id = input('Input new id for section:')
                    self.sections[i].id = new_id
                    for j in range(len(self.goods)):
                        if self.goods[j].section_code == old_id:
                            self.goods[j].section_code = new_id
                elif setting == 3:
                    new_name = input('Input new name for section:')
                    self.sections[i].name = new_name
                else:
                    raise exceptions.InputError('Error input: please choose parameters between 1 and 2')
        if not is_section:
            raise exceptions.NonSectionError

    def edit_goods(self, id):
        print('Please select the setting you want to change in goods:')
        print('1 - id')
        print('2 - name')
        print('3 - price')
        print('4 - goods type')
        setting = int(input())
        is_goods = False
        for i in range(len(self.goods)):
            if self.goods[i].id == id:
                is_goods = True
                if setting == 1:
                    new_id = input('Input new id for goods:')
                    self.goods[i].id = new_id
                elif setting == 2:
                    new_name = input('Input new name for goods:')
                    self.goods[i].name = new_name
                elif setting == 3:
                    new_price = input('Input new price for goods:')
                    self.goods[i].price = new_price
                elif setting == 4:
                    new_goods_type = input('Input new goods type for goods:')
                    self.goods[i].goods_type = new_goods_type
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
        for i in range(len(self.sections)):
            print('id:', self.sections[i].id, ', name:', self.sections[i].name)

    def get_all_list_goods(self, section_code):
        is_section = False
        for i in range(len(self.sections)):
            if self.sections[i].id == section_code:
                is_section = True
                for j in range(len(self.goods)):
                    if self.goods[j].section_code == section_code:
                        print('id:', self.goods[j].id, ', name:', self.goods[j].name,
                              ', price:', self.goods[j].price, ', goods type:', self.goods[j].goods_type)
        if not is_section:
            raise exceptions.NonSectionError
