class Flower:
    def __init__(self, name, color, stem_length, freshness, price):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.freshness = freshness
        self.price = price


class Rose(Flower):
    def __init__(self, color, stem_length, freshness, price):
        super().__init__("Роза", color, stem_length, freshness, price)


class Chamomile(Flower):
    def __init__(self, color, stem_length, freshness, price):
        super().__init__("Ромашка", color, stem_length, freshness, price)


class Bouquet:
    def __init__(self):
        self.flowers = []  # Создание списка для букета

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_wilting_time(self):
        return sum(flower.freshness for flower in self.flowers) / len(self.flowers)

    def calculate_total_price(self):
        return sum(flower.price for flower in self.flowers)

    def sort_by_color(self):
        self.flowers.sort(key=lambda x: x.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda x: x.stem_length)

    def sort_by_price(self):
        self.flowers.sort(key=lambda x: x.price)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda x: x.freshness)

    def search_flowers_by_parameter(self, parameter):  # Поиск цветов по параметру (свежести)
        return [flower for flower in self.flowers if parameter == flower.__dict__['freshness']]


roses = [Rose("красная", 10, 8, 8), Rose("синяя", 12, 7, 9)]
chamomiles = [Chamomile("белая", 15, 7, 5), Chamomile("желтая", 14, 8, 12)]

bouquet = Bouquet()
bouquet.flowers.extend(roses + chamomiles)

print("Среднее время увядания:", bouquet.calculate_wilting_time())

bouquet.sort_by_color()
print("Сортировка по цвету:", [flower.color for flower in bouquet.flowers])

bouquet.sort_by_stem_length()
print("Сортировка по длине стебля:", [flower.stem_length for flower in bouquet.flowers])

bouquet.sort_by_price()
print("Сортировка по цене:", [flower.price for flower in bouquet.flowers])

bouquet.sort_by_freshness()
print("Сортировка по свежести:", [flower.freshness for flower in bouquet.flowers])

result = bouquet.search_flowers_by_parameter(8)
print("Поиск цветов по параметру свежести 8:", [flower.name for flower in result])
