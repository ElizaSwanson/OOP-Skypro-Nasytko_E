from src.lawngrass_class import LawnGrass
from src.product_class import Product
from src.smartphone_class import Smartphone
import pytest


def test_print_smartphone(capsys):
    Smartphone("Samsung Galaxy S23 Ultra","256GB, Серый цвет, 200MP камера",180000.0,5,95.5,"S23 Ultra",256,"Серый")

    res = capsys.readouterr()
    assert res.out.strip() == "Smartphone (Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

def test_print_lawngrass(capsys):
    LawnGrass(
    "Газонная трава",
    "Элитная трава для газона",
    500.0,
    20,
    "Россия",
    "7 дней",
    "Зеленый",
)

    res = capsys.readouterr()
    assert res.out.strip() == "LawnGrass (Газонная трава, Элитная трава для газона, 500.0, 20)"

def test_print_prod(capsys):
    Product("Новелла", "САМОЕ КРУТОЕ ЧТО ТЫ ЧИТАЛ!!!", 550, 100)

    res = capsys.readouterr()
    assert res.out.strip() == "Product (Новелла, САМОЕ КРУТОЕ ЧТО ТЫ ЧИТАЛ!!!, 550, 100)"

if __name__ == "__main__":
    pytest.main()

