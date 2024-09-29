from src.lawngrass_class import LawnGrass
import pytest

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


def test_lawngrass():
    assert grass1.name == "Газонная трава"
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_sum():
    assert grass1 + grass2 == 16750


def test_error():
    assert grass1 + 1 == TypeError


if __name__ == "__main__":
    pytest.main()
