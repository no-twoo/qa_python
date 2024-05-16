import pytest

from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_duplicate_not_added(self):
        # Arrange
        collector = BooksCollector()
        collector.add_new_book('Игра престолов')

        # Act
        collector.add_new_book('Игра престолов')

        # Assert
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_two_books_added(self):
        # Arrange
        collector = BooksCollector()

        # Act
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # Assert
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['', 'Книга в названии которой больше сорока одного символа'])
    def test_add_new_book_not_added(self, name):
        # Arrange
        collector = BooksCollector()

        # Act
        collector.add_new_book(name)

        # Assert
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_one_genre_added(self):
        # Arrange

        collector = BooksCollector()
        expected_book = 'Игра престолов'
        expected_genre = 'Фантастика'
        collector.add_new_book(expected_book)

        # Act
        collector.set_book_genre(expected_book, expected_genre)

        # Assert
        assert collector.get_book_genre(expected_book) == expected_genre

    def test_get_book_genre_one_genre_got(self):
        # Arrange

        collector = BooksCollector()
        expected_book = 'Игра престолов'
        expected_genre = 'Фантастика'
        collector.add_new_book(expected_book)
        collector.set_book_genre(expected_book, expected_genre)

        # Act
        actual_genre = collector.get_book_genre(expected_book)

        # Assert
        assert expected_genre == actual_genre

    def test_get_books_with_specific_genre_two_books(self):
        # Arrange
        collector = BooksCollector()
        expected_book1 = 'Гордость и предубеждение и зомби'
        expected_book2 = 'Что делать, если ваш кот хочет вас убить'
        expected_genre = 'Фантастика'

        expected_books_names = [expected_book1, expected_book2]
        collector.add_new_book(expected_book1)
        collector.add_new_book(expected_book2)
        collector.set_book_genre(expected_book1, expected_genre)
        collector.set_book_genre(expected_book2, expected_genre)

        # Act
        actual_books_with_specific_genre = collector.get_books_with_specific_genre(expected_genre)

        # Assert
        assert expected_books_names == actual_books_with_specific_genre

    def test_get_books_genre_any_books(self):
        # Arrange
        collector = BooksCollector()

        expected_book1 = 'Гордость и предубеждение и зомби'
        expected_book2 = 'Что делать, если ваш кот хочет вас убить'
        collector.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        collector.add_new_book(expected_book1)
        collector.add_new_book(expected_book2)
        collector.set_book_genre(expected_book1, 'Фантастика')
        collector.set_book_genre(expected_book2, 'Детективы')

        expected_genre = {
            expected_book1: 'Фантастика',
            expected_book2: 'Детективы',
        }

        # Act
        actual_books_genre = collector.get_books_genre()

        # Assert
        assert expected_genre == actual_books_genre

    def test_get_books_for_children_two_books(self):
        # Arrange
        collector = BooksCollector()

        expected_books_names = ['Смешарики', 'Маша и Медведь']
        collector.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        collector.add_new_book('Смешарики')
        collector.add_new_book('Маша и Медведь')
        collector.set_book_genre('Смешарики', 'Комедии')
        collector.set_book_genre('Маша и Медведь', 'Мультфильмы')

        # Act
        actual_books_for_children = collector.get_books_for_children()

        # Assert
        assert expected_books_names == actual_books_for_children

    def test_get_books_for_children_book_not_added(self):
        # Arrange
        collector = BooksCollector()

        collector.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        collector.add_new_book('Астрал')
        collector.set_book_genre('Астрал', 'Ужасы')

        # Act
        actual_books_for_children = collector.get_books_for_children()

        # Assert
        assert collector.get_books_genre() != actual_books_for_children

    def test_add_book_in_favorites_one_book_added(self):
        # Arrange
        collector = BooksCollector()
        expected_book = 'Игра престолов'
        collector.add_new_book(expected_book)

        # Act
        collector.add_book_in_favorites(expected_book)

        # Assert
        assert len(collector.get_list_of_favorites_books()) == 1
        assert collector.get_list_of_favorites_books()[0] == expected_book

    def test_delete_book_from_favorites_one_book(self):
        # Arrange
        collector = BooksCollector()
        expected_name_1 = 'Игра престолов'
        expected_name_2 = 'Властелин колец'
        collector.add_new_book(expected_name_1)
        collector.add_new_book(expected_name_2)
        collector.add_book_in_favorites(expected_name_1)
        collector.add_book_in_favorites(expected_name_2)

        # Act
        collector.delete_book_from_favorites(expected_name_2)

        # Assert
        assert len(collector.get_list_of_favorites_books()) == 1
        assert collector.get_list_of_favorites_books()[0] == expected_name_1

    def test_get_list_of_favorites_books_two_books(self):
        # Arrange
        collector = BooksCollector()
        expected_favorites_books = ['Игра престолов', 'Властелин колец']
        collector.add_new_book('Игра престолов')
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Игра престолов')
        collector.add_book_in_favorites('Властелин колец')

        # Act
        actual_list_of_favorites_books = collector.get_list_of_favorites_books()

        # Assert
        assert expected_favorites_books == actual_list_of_favorites_books
