name = "Вино из одуванчиков"
name2 = "Время колокольчиков"
rating = 7


class TestBooksCollector:

    # проверяем, что добавились две книги
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book(name)
        collector.add_new_book(name2)
        assert len(collector.get_books_rating()) == 2

    # проверяем, что параметр books_rating по умолчанию пустой
    def test_default_value_books_rating_empty(self, collector):
        assert collector.books_rating == {}

    # проверяем, что параметр favorites по умолчанию пустой
    def test_default_value_favorites_empty(self, collector):
        assert collector.favorites == []

    # проверяем, что в словаре добавлена книга с рейтингом 1
    def test_add_new_book_is_added(self, collector):
        collector.add_new_book(name)
        assert collector.books_rating[name] == 1

    # проверяем, что установлен рейтинг книге (от 1 до 10)
    def test_set_book_rating_successful(self, collector):
        collector.add_new_book(name)
        collector.set_book_rating(name, rating)
        assert collector.books_rating[name] == rating

    # проверяем, что можно получить рейтинг книги по ее имени
    def test_get_book_rating_successful(self, collector):
        collector.add_new_book(name)
        collector.set_book_rating(name, rating)
        assert collector.get_book_rating(name) == rating

    # проверяем, что доступен вывод списка книг с определенным рейтингом
    def test_get_books_with_specific_rating_successful(self, collector):
        collector.add_new_book(name)
        collector.set_book_rating(name, rating)
        assert collector.get_books_with_specific_rating(rating) == ['Вино из одуванчиков']

    # проверяем, что можно получить словарь books_rating
    def test_get_books_rating_successful(self, collector):
        collector.add_new_book(name)
        collector.set_book_rating(name, rating)
        print(collector.get_books_rating())
        assert collector.get_books_rating() == {'Вино из одуванчиков': 7}

    # проверяем, что книгу можно добавить в избранное
    def test_add_book_in_favorites_successful(self, collector):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.favorites[0] == 'Вино из одуванчиков'

    # проверяем, что книгу можно удалить из избранного
    def test_delete_book_from_favorites_successful(self, collector):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert collector.favorites == []

    # проверяем, что можно получить список избранных книг
    def test_get_list_of_favorites_books_successful(self, collector):
        collector.add_new_book(name)
        collector.add_new_book(name2)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name2)
        print(collector.favorites)
        assert collector.get_list_of_favorites_books() == ['Вино из одуванчиков', 'Время колокольчиков']


