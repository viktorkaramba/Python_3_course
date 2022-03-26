import lxml.etree
from lxml import etree


def validate(xml_path, xsd_path):
    xml_validator = etree.XMLSchema(file=xsd_path)
    xml_file = lxml.etree.parse(xml_path)
    is_valid = xml_validator.validate(xml_file)
    return is_valid
