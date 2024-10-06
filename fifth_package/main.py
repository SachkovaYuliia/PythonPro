from xml_operations import read_products, update_product_quantity

def main():
    filename = 'products.xml'

    print(f"Using file: {filename}")

    read_products(filename)

    product_name = input("Введіть назву продукту для зміни кількості: ")
    new_quantity = int(input("Введіть нову кількість: "))
    update_product_quantity(filename, product_name, new_quantity)

    read_products(filename)

if __name__ == "__main__":
    main()
