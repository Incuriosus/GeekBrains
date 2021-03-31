class Clothes:
    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.v = float(size)
        self.consumption = self.v/6.5 + 0.5


class Costume(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.h = float(height)
        self.consumption = self.h * 2 + 0.3


class AllProducts:
    def __init__(self):
        self._products = set()

    def __iter__(self):
        return (el for el in self._products)

    def add(self, product):
        self._products.add(product)

    def remove(self, product):
        if product in self._products:
            self._products.remove(product)
        else:
            print('Данный продукт не добавлен')

    @property
    def consumption(self):
        result = 0
        for i in self._products:
            result += i.consumption
        return result


if __name__ == '__main__':
    costume_1 = Costume('Tailcoat', 6.1)
    print(costume_1.h, costume_1.name)
    coat_1 = Coat('Cape Coat', 54)
    print(coat_1.v, coat_1.name)
    all_products = AllProducts()
    all_products.add(costume_1)
    all_products.add(coat_1)
    print(all_products.consumption)
    print(coat_1 in all_products)
