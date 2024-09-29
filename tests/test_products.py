import pytest

from src.product_class import Product


str_test = Product("Новелла", "САМОЕ КРУТОЕ ЧТО ТЫ ЧИТАЛ!!!", 550, 100)


def test_prod():
    assert str_test.name == "Новелла"
    assert str_test.description == "САМОЕ КРУТОЕ ЧТО ТЫ ЧИТАЛ!!!"
    assert str_test.price == 550
    assert str_test.quantity == 100


def test_new_product():
    new = Product("Снайпер", "Автобиография самого смертоносного снайпера", 400, 300)
    new.price = 0
    assert new.price == 400
    new.price = 500
    assert new.price == 500


def test_str():
    assert str(str_test) == "Новелла, 550 руб. Остаток: 100 шт."

sniper = Product("Снайпер", "Крутое чтиво", 550, 100)
elven_lied = Product("Elven lied", "Manga", 700, 10)

def test_add():
    assert sniper + elven_lied == "Всего товаров на сумму: 62000"


if __name__ == "__main__":
    pytest.main()
