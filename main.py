class Basket:
    def __init__(self):
        self.data = []

    def add(self, product, price):
        self.data.append({'product': product, 'price': price})
        print(f"{product} ({price}) savatga qo'shildi")

    def remove(self, product):
        for item in self.data:
            if item['product'] == product:
                self.data.remove(item)
                print(f"{product} savatdan olib tashlandi")
                return
        print(f"{product} savatda topilmadi")

    def show(self):
        if not self.data:
            print("Savat bo'sh")
        else:
            print("Savat tarkibi")
            for item in self.data:
                print(f"- {item['product']}: {item['price']}")

    def calculating(self):
        total = sum(item['price'] for item in self.data)
        print(f"Umumiy narx: {total}")


basket = Basket()
basket.add("Banan", 1)
basket.add("Banan", 1)
basket.show()
basket.calculating()
basket.remove("Banan")
basket.show()
