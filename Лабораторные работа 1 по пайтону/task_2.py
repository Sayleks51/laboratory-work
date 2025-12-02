# TODO Найдите количество книг, которое можно разместить на дискете
size = 1.44 # Информационный объем
page = 100 # Страницы
line = 50 # Строка
symbol = 25 # Символ
bytes = 4 # Байт
one_Kbyte = 1024 # Один Килобайт
one_Mbyte = 1024 # Один Мегабайт

number_of_characters = page * line * symbol # Символов

total_size_book = number_of_characters * bytes # Кбайт

conversion = total_size_book / (one_Mbyte*one_Kbyte) # Мбайт

books = int(size // conversion) # Книги

print("Количество книг, помещающихся на дискету:", books)
