import pytest

from src.category_class import Category
from src.product_class import Product

sniper = Product("Снайпер", "Крутое чтиво", 550, 100)
elven_lied = Product("Elven lied", "Manga", 700, 10)
category_test = Category("Книга", "Книги - источник знаний!", [elven_lied])


@pytest.fixture
def f_c():
    return Category("Книга", "Книги - источник знаний!", {sniper})


sniper = Product("Снайпер", "Крутое чтиво", 550, 100)


def test_category(f_c):
    assert f_c.name == "Книга"
    assert f_c.description == "Книги - источник знаний!"
    assert f_c.products == "Снайпер, 550 руб. Остаток: 100 шт.\n"
    assert Category.category_count == 2
    assert Category.product_count == 2


def test_str():
    assert str(category_test) == "Книга, количество продуктов: 10"


if __name__ == "__main__":
    pytest.main()
