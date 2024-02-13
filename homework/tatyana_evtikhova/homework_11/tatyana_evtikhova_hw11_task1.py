# Первый класс
class Book:
    def __init__(self, material, has_text, title, author, num_pages, isbn):
        self.material = material
        self.has_text = has_text
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved = False

    def __str__(self):
        reserved_status = 'зарезервирована' if self.reserved else 'не зарезервирована'
        return (f"Название: {self.title}, Автор: {self.author}, страниц: {self.num_pages}, материал {self.material}, "
                f"{reserved_status}")


book1 = Book("бумага", True, "Преступление и наказание", "Достоевский", 400,
             "978-5-17-090004-5")
book2 = Book("бумага", True, "Война и мир", "Толстой", 1225,
             "978-5-699-71574-0")
book3 = Book("бумага", True, "Гарри Поттер и философский камень", "Роулинг", 332,
             "978-5-699-71574-0")
book4 = Book("бумага", True, "1984", "Оруэлл", 328,
             "978-5-699-71574-0")
book5 = Book("бумага", True, "Мастер и Маргарита", "Булгаков", 432,
             "978-5-699-71574-0")

book1.reserved = True
book5.reserved = True

print(book1)
print(book2)
print(book3)
print(book4)
print(book5)

# Второй класс

class Schoolbook(Book):
    def __init__(self, material, has_text, title, author, num_pages, isbn, subject, group, has_tasks):
        super().__init__(material, has_text, title, author, num_pages, isbn)
        self.subject = subject
        self.group = group
        self.has_tasks = has_tasks

    def __str__(self):
        reserved_status = 'зарезервирована' if self.reserved else 'не зарезервирована'
        return (
            f"Название: {self.title}, Автор: {self.author}, страниц: {self.num_pages}, "
            f"предмет: {self.subject}, класс: {self.group}, {reserved_status}"
        )


schoolbook1 = Schoolbook("бумага", True, "Алгебра", "Иванов", 200,
                         "978-5-699-75574-0", "Математика", 9, True)
schoolbook2 = Schoolbook("бумага", True, "Физика", "Формулов", 180,
                         "978-5-699-71444-1", "Физика", 10, True)
schoolbook3 = Schoolbook("бумага", True, "История", "Параграфов", 250,
                         "978-5-699-71574-1", "История", 11, False)
schoolbook4 = Schoolbook("бумага", True, "Биология", "Цветочкин", 160,
                         "978-5-699-70074-2", "Биология", 9, True)
schoolbook5 = Schoolbook("бумага", True, "География", "Европин", 220,
                         "978-5-699-72274-3", "География", 8, False)

schoolbook2.reserved = True

print(schoolbook1)
print(schoolbook2)
print(schoolbook3)
print(schoolbook4)
print(schoolbook5)
