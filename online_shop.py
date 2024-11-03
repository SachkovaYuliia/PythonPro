# 1. Створення бази даних та колекцій:
# Створіть базу даних для зберігання інформації про онлайн-магазин.
# Створіть колекцію products, яка містить дані про продукти (назва, ціна, категорія, кількість на складі).
# Створіть колекцію orders, яка містить інформацію про замовлення (номер замовлення, клієнт, список продуктів із кількістю, загальна сума).

# 2. CRUD операції:
# Create: Додайте кілька продуктів і замовлень у відповідні колекції.
# Read: Витягніть всі замовлення за останні 30 днів.
# Update: Оновіть кількість продукту на складі після його купівлі.
# Delete: Видаліть продукти, які більше не доступні для продажу.

# 3. Агрегація даних:
# Порахуйте загальну кількість проданих продуктів за певний період часу.
# Використовуйте функцію агрегації для підрахунку загальної суми всіх замовлень клієнта.

# 4. Індекси:
# Додайте індекси для поля category в колекції products, щоб прискорити пошук продуктів по категоріях.

from pymongo import MongoClient
from datetime import datetime, timedelta


"""
Підключення до MongoDB
"""
client = MongoClient("mongodb://localhost:27017/")  
db = client["online_shop"]

"""
Колекції для продуктів і замовлень
"""
products_collection = db['products']
orders_collection = db['orders']

products = [
    {"name": "Iphone16 Pro", "price": 47500, "category": "Smartphones", "stock": 10},
    {"name": "Ipad Pro11", "price": 63000, "category": "Ipads", "stock": 20},
    {"name": "Macbook Air", "price": 50000, "category": "Notebooks", "stock": 30},
    {"name": "Apple AirPods Max", "price": 25500, "category": "Airpods", "stock": 40},
    {"name": "Apple AirPods", "price": 25000, "category": "Airpods", "stock": 0}
]

"""
Додавання продуктів
"""
products_collection.insert_many(products)


def create_order(order_id, customer, order_products):
    """
    Функція для створення замовлення
    """
    total_price = 0
    order_items = []
    
    """
    Обробка кожного продукту в замовленні
    """
    for item in order_products:
        product = products_collection.find_one({"name": item["name"]})
        if product:
            
            """
            Перевірка наявності товару на складі
            """
            if product["stock"] >= item["quantity"]:

                """
                Оновлення запасів на складі
                """
                products_collection.update_one(
                    {"name": item["name"]},
                    {"$inc": {"stock": -item["quantity"]}}
                )

                """
                Обчислення загальної ціни для продукту
                """
                item_total = product["price"] * item["quantity"]
                total_price += item_total
                order_items.append({
                    "name": item["name"],
                    "quantity": item["quantity"],
                    "unit_price": product["price"],
                    "total_price": item_total
                })
            else:
                print(f"Недостатньо товару '{item['name']}' на складі.")
        else:
            print(f"Продукт '{item['name']}' не знайдено.")
    
    """
    Формування замовлення
    """
    order = {
        "order_id": order_id,
        "customer": customer,
        "products": order_items,
        "total_price": total_price,
        "date": datetime.now()
    }

    """
    Додавання замовлення в колекцію
    """
    orders_collection.insert_one(order)
    print(f"Замовлення {order_id} додано з загальною сумою {total_price}.")


order_products = [
    {"name": "Iphone16 Pro", "quantity": 1},
    {"name": "Apple AirPods Max", "quantity": 2}
]

create_order(order_id=2, customer="Test Test", order_products=order_products)


def get_orders_last_30_days():
    """
    Функція отримання замовлень за останні 30 днів.
    """
    thirty_days_ago = datetime.now() - timedelta(days=30)
    orders = orders_collection.find({"date": {"$gte": thirty_days_ago}})
    
    for order in orders:
        print(order)

get_orders_last_30_days()


def update_product_stock(product_name, quantity):
    """
    Функція оновлення кількості продукту на складі після його купівлі.
    """
    products_collection.update_one(
        {"name": product_name},
        {"$inc": {"stock": -quantity}}
    )
    print(f"Кількість продукту '{product_name}' зменшено на {quantity}.")

update_product_stock("Iphone16 Pro", 9)


def delete_unavailable_products():
    """
    Функція видалення продукції, яка більше не доступна для продажу.
    """
    result = products_collection.delete_many({"stock": 0})
    print(f"Видалено продуктів: {result.deleted_count}")

delete_unavailable_products()


def count_total_sold_products(start_date, end_date):
    """
    Функція агрегації даних.
    """
    pipeline = [
        #Фільтрація замовлень за вказаний період
        {"$match": {"date": {"$gte": start_date, "$lte": end_date}}},
        
        #Розгортання масиву продуктів у замовленні
        {"$unwind": "$products"},

        #Групування та підрахунок загальної кількості проданих одиниць
        {"$group": {
            "_id": None,
            "total_sold": {"$sum": "$products.quantity"}
        }}
    ]
    
    result = list(orders_collection.aggregate(pipeline))
    total_sold = result[0]["total_sold"] if result else 0
    print(f"Загальна кількість проданих продуктів за вказаний період: {total_sold}")

"""
Виклик функцій
""" 
start_date = datetime.now() - timedelta(days=30)
end_date = datetime.now()
count_total_sold_products(start_date, end_date)

""" 
Створення колекції для категорій
"""
categories_collection = db["categories"]

def get_or_create_category_id(category_name):
    """
    Функція для створення індексу
    """
    category = categories_collection.find_one({"name": category_name})
    
    # Якщо категорія вже є, повертаємо її індекс
    if category:
        return category["category_id"]
    
    # Якщо категорії немає, створюємо її з новим індексом
    new_category_id = categories_collection.count_documents({}) + 1  
    categories_collection.insert_one({"name": category_name, "category_id": new_category_id})
    
    return new_category_id


"""
Оновлення колекції "products"в частині додавання індексу до кожного продукту
"""
for product in products_collection.find({}):
    category_id = get_or_create_category_id(product["category"])
    products_collection.update_one(
        {"_id": product["_id"]},
        {"$set": {"category_id": category_id}}
    )

print("Категорії створені, та `category_id` додано до продуктів.")


def list_all_categories():
    """
    Функція для виведення всіх категорій та їх індексів
    """
    categories = categories_collection.find({})
    print("Список категорій та їх ID:")
    for category in categories:
        print(f"Категорія: {category['name']}, ID: {category['category_id']}")

list_all_categories()


def find_products_by_category_id(category_id):
    """
    Функція для пошуку товарів за індексом
    """
    products = products_collection.find({"category_id": category_id})
    print(f"Товари у категорії з ID '{category_id}':")
    for product in products:
        print(product)

find_products_by_category_id(4)  