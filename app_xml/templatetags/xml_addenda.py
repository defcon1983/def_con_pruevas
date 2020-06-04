from django import template
from xml.etree.ElementTree import parse, Element

register = template.Library()
xml_docto = parse(
    'C:/Users/drago/OneDrive/Escritorio/ataque_xml/addenda/app_xml/templatetags/datos.xml')

raiz = xml_docto.getroot()

e = Element('nombre')
e.text = 'indicame el contenido de elemento'
raiz.insert(700, e)

xml_docto.write('nuevo_docto_xml.xml', xml_declaration=True)
