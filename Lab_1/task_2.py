storage_Mb = 1.44# TODO Найдите количество книг, которое можно разместить на дискете
cnt_pages = 100
cnt_strings = 50
cnt_symbols = 25
one_symbol_b = 4
storage_b = storage_Mb * 1024 * 1024
cnt_books =round(storage_b / (cnt_pages * cnt_strings * cnt_symbols * one_symbol_b))
print("Количество книг, помещающихся на дискету:", cnt_books)
