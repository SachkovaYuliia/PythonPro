import xml.etree.ElementTree as ET
import json


def read_products(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        print("Продукти в магазині:")
        for product in root.findall('product'):
            name = product.find('name').text
            quantity = product.find('quantity').text
            print(f"Назва: {name}, Кількість: {quantity}")

    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")


def update_product_quantity(filename, product_name, new_quantity):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        for product in root.findall('product'):
            name = product.find('name').text
            if name == product_name:
                product.find('quantity').text = str(new_quantity)
                print(f"Кількість товару '{product_name}' змінено на {new_quantity}.")
                break
        else:
            print(f"Продукт '{product_name}' не знайдено.")

        tree.write(filename, encoding='utf-8', xml_declaration=True)

    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")


def xml_to_json(xml_filename, json_filename):
    try:
        tree = ET.parse(xml_filename)
        root = tree.getroot()

        products = []
        for product in root.findall('product'):
            product_data = {
                'name': product.find('name').text,
                'price': float(product.find('price').text),
                'quantity': int(product.find('quantity').text)
            }
            products.append(product_data)

        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(products, json_file, ensure_ascii=False, indent=4)

        print(f"Файл {xml_filename} успішно перетворено у {json_filename}.")

    except FileNotFoundError:
        print(f"Файл {xml_filename} не знайдено.")


def json_to_xml(json_filename, xml_filename):
    try:
        with open(json_filename, 'r', encoding='utf-8') as json_file:
            products = json.load(json_file)

        root = ET.Element("products")

        for product in products:
            product_element = ET.Element("product")

            name = ET.SubElement(product_element, "name")
            name.text = product['name']

            price = ET.SubElement(product_element, "price")
            price.text = str(product['price'])

            quantity = ET.SubElement(product_element, "quantity")
            quantity.text = str(product['quantity'])

            root.append(product_element)

        tree = ET.ElementTree(root)
        tree.write(xml_filename, encoding='utf-8', xml_declaration=True)

        print(f"Файл {json_filename} успішно перетворено у {xml_filename}.")

    except FileNotFoundError:
        print(f"Файл {json_filename} не знайдено.")

