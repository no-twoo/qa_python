# qa_python
    - test_add_new_book_duplicate_not_added
        проверяет, что метод не добавит в словарь несколько раз книгу с одинаковым названием

    - test_add_new_book_two_books_added
        проверяет, что метод добовляет книги в словарь

    - test_add_new_book_not_added
        проверяет, что метод не добавит в словарь книгу, у которой длинна названия не соответствует заданным параметрам

    - test_set_book_genre_one_genre_added
        проверяет, что метод устанавливает книге жанр

    - test_get_book_genre_one_genre_got
        проверяет, что метод получает жанр книги по названию

    - test_get_books_with_specific_genre_two_books
        проверяет, что метод выводит список книг по опредленному жанру

    - test_get_books_genre_any_books
        проверяет, что метод возвращает словарь с названиями и жанрами книг

    - test_get_books_for_children_two_books
        проверяет, что метод возвращает книги, подходящие для детей

    - test_get_books_for_children_book_not_added
        проверяет, что метод не возвращает книги с запрещенными для детей жанрами

    - test_add_book_in_favorites_one_book_added
        проверяет, что метод добавляет книгу в Избранное

    - test_delete_book_from_favorites_one_book
        проверяет, что метод удаляет книгу из Избранного

    - test_get_list_of_favorites_books_two_books
        проверяет, что метод возвращает список Избранных книг
