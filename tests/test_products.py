import pytest

from src.category_class import Category
from src.product_class import Product


@pytest.fixture
def f_p():
    return Product("Новелла", "САМОЕ КРУТОЕ ЧТО ТЫ ЧИТАЛ!!!", 550, 100)


def test_prod(f_p):
    assert f_p.name == "Новелла"
    assert f_p.description == "САМОЕ КРУТОЕ ЧТО ТЫ ЧИТАЛ!!!"
    assert f_p.price == 550
    assert f_p.quantity == 100


def test_new_product():
    new = Product("Снайпер",
            "Автобиография самого смертоносного снайпера",
            400,
            300
        )
    new.price = 0
    assert new.price == 400
    new.price = 500
    assert new.price == 500


if __name__ == "__main__":
    pytest.main()