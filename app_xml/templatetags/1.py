from xml.etree.ElementTree import parse, Element
from django import template

register = template.Library()

documento = parse(
    'C:/Users/drago/OneDrive/Escritorio/ataque_xml/addenda/app_xml/templatetags/datos.xml')

raiz = documento.getroot()

e = Element('DEF_CON')
e.text = 'TEXTO DE PUEBAS DEL NODO'
raiz.insert(5000, e)

documento.write('datos-nuevos.xml', xml_declaration=True)
