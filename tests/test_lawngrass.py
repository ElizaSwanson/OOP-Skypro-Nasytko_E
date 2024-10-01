import pytest

from src.lawngrass_class import LawnGrass
from src.smartphone_class import Smartphone

grass1 = LawnGrass(
    "Газонная трава",
    "Элитная трава для газона",
    500.0,
    20,
    "Россия",
    "7 дней",
    "Зеленый",
)
grass2 = LawnGrass(
    "Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый"
)

smartphone1 = Smartphone(
    "Samsung Galaxy S23 Ultra",
    "256GB, Серый цвет, 200MP камера",
    180000.0,
    5,
    95.5,
    "S23 Ultra",
    256,
    "Серый",
)


def test_lawngrass():
    assert grass1.name == "Газонная трава"
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_sum():
    assert grass1 + grass2 == 16750


def test_error_1():
    with pytest.raises(TypeError):
        res1 = grass1 + smartphone1
        res2 = grass1 + 1
        res1 == TypeError
        res2 == TypeError


if __name__ == "__main__":
    pytest.main()
