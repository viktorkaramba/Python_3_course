import sax_parser as sp
import exceptions
import validator

if __name__ == '__main__':
    parser = sp.xml.sax.make_parser()
    parser.setFeature(sp.xml.sax.handler.feature_namespaces, 0)
    handler = sp.StorageHandler()
    parser.setContentHandler(handler)
    parser.parse("xml/storage.xml")
    if validator.validate('xml/storage.xml', 'xml/storage.xsd'):
        try:
            handler.storage.add_section('3', 'Candies')
            handler.storage.add_goods('5', 'Raffaello', '100', '3', 'Chocolate')
            handler.storage.add_goods('6', 'Cracker', '42', '3', 'Cookies')
            handler.storage.save_to_file('xml/storage.xml')
            handler.storage.get_all_list_sections()
            handler.storage.delete_section('3')
            handler.storage.save_to_file('xml/storage.xml')
            handler.storage.get_all_list_sections()
            print(handler.storage.get_section_ind(1).id, handler.storage.get_section_ind(1).name)
            handler.storage.edit_section('1')
            handler.storage.get_all_list_sections()
            handler.storage.edit_goods('4')
            handler.storage.get_all_list_goods('2')
            handler.storage.delete_goods('8')
            handler.storage.get_all_list_goods('2')
            handler.storage.save_to_file('xml/storage.xml')
            handler.storage.edit_section('4')
            handler.storage.save_to_file('xml/storage.xml')
            handler.storage.add_goods('4', 'PS 5', '750', '2', 'game console')
            handler.storage.save_to_file('xml/storage.xml')
        except exceptions.MyException as e:
            print(e)
