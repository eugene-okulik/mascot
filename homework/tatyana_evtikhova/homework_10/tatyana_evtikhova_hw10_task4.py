PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_list_by_lines = PRICE_LIST.split('\n')
price_dict = {item.split()[0]: int(item.split()[1][:-1]) for item in price_list_by_lines}

print(price_dict)
