import pytest

from src.classes import Category
from src.product_class import Product


@pytest.fixture
def f_c():
    return Category("Книга", "Книги - источник знаний!", ["みんなの日本語", "Противостояние - С. Кинг"])

@pytest.fixture
def f_p():
    return Product("Новелла", "САМОЕ КРУТОЕ ЧТО ТЫ ЧИТАЛ!!!", 550, 100)

@pytest.fixture
def new():
    return Product("Снайпер", "Автобиография самого смертоносного снайпера", 400,4300,)


def test_category(f_c):
    assert f_c.name == "Книга"
    assert f_c.description == "Книги - источник знаний!"
    assert f_c.products[0] == "みんなの日本語"
    assert Category.category_count == 1
    assert Category.product_count == 2

def test_prod(f_p):
    assert f_p.name == "Новелла"
    assert f_p.description == "САМОЕ КРУТОЕ ЧТО ТЫ ЧИТАЛ!!!"
    assert f_p.price == 550
    assert f_p.quantity == 100

def test_new_product():
    new.price = 500
    assert new.price == 500


if __name__ == "__main__":
    pytest.main()