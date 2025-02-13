import uuid

class Product:
    def __init__(self, name, price, quantity):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.quantity = quantity

    def info(self):
        return f"ID: {self.id} | Mahsulot: {self.name} | Narx: {self.price} | Mavjud: {self.quantity}"

    def sell(self, amount):
        if amount > self.quantity:
            print(f"Bizda {self.quantity} ta mahsulot bor")
        else:
            self.quantity -= amount

    def restock(self, amount):
        self.quantity += amount


class Electronics(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def info(self):
        return super().info() + f" | Kafolat: {self.warranty}"


class Food(Product):
    def __init__(self, name, price, quantity, surok):
        super().__init__(name, price, quantity)
        self.surok = surok

    def info(self):
        return super().info() + f" | Yaroqlilik muddati: {self.surok}"



class Basket:
    def __init__(self):
        self.data = {}

    def add(self, product):
        self.data[product.id] = {'product': product, 'price': product.price}
        print(f"{product.name} ({product.price}) savatga qo'shildi | ID: {product.id}")

    def remove(self, product_id):
        if product_id in self.data:
            product_name = self.data[product_id]['product'].name
            del self.data[product_id]
            print(f"{product_name} savatdan olib tashlandi")
        else:
            print(f"ID: {product_id} bo'lgan mahsulot savatda topilmadi")

    def show(self):
        if not self.data:
            print("Savat bo'sh")
        else:
            print("Savat tarkibi:")
            for product_id, item in self.data.items():
                print(f"- {item['product'].name} (ID: {product_id}): {item['price']}")

    def calculating(self):
        total = sum(item['price'] for item in self.data.values())
        print(f"Umumiy narx: {total}")
