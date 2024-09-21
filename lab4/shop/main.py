catalog = {'яблоко': 10, 'банан': 20, 'персик': 30}

class Cart:
    def __init__(self):
        self.goods = {}
        global catalog
        self.catalog = catalog

    def add(self, name, count):
        self.goods[name] = self.goods.get(name, 0) + count

    def count(self):
        return sum(self.goods.values())

    def total(self):
        return sum([self.catalog[key] * value for key, value in self.goods.items()])

def main():
    cart = Cart()
    while True:
        print('Каталог:')
        for i, (name, price) in enumerate(catalog.items(), 1):
            print('{}) {} - {}'.format(i, name, price))
        print('{} - просмотр корзины'.format(len(catalog) + 1))
        print('{} - выход'.format(len(catalog) + 2))
        choice = int(input('Выберите товар: '))

        if choice == len(catalog) + 1:
            print('Ваша корзина:')
            for i, (name, count) in enumerate(cart.goods.items(), 1):
                print('{}) {} - {}'.format(i, name, count))
        elif choice == len(catalog) + 2:
            break
        else:
            name = list(catalog.keys())[choice - 1]
            count = int(input('Введите количество: '))
            cart.add(name, count)
            print('В корзине {} товаров, общая сумма: {}'.format(cart.count(), cart.total()))

if __name__ == '__main__':
    main()

