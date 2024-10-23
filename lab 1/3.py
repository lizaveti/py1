# TODO Найдите количество книг, которое можно разместить на дискете

disketa = 1.44 * 1024 * 1024
pages = 100
strs = 50
chars = 25
ves = 4

book = ves * chars * strs * pages
res = disketa // book

print("Количество книг, помещающихся на дискету:", int(res))
