from models import Electronics, Food
from models import Basket


laptop = Electronics("Laptop", 1500, 5, "2 yil")
apple = Food("Olma", 2, 50, "1 oy")

basket = Basket()
basket.add(laptop)
basket.add(apple)
basket.show()
basket.remove(laptop.id)
basket.show()
basket.calculating()
