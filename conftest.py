from unittest.mock import Mock
import pytest
import data
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture()  # объект класса Bun
def bun():
    bun = Bun(data.BUN_NAME, data.BUN_PRICE)
    return bun


@pytest.fixture()
def ingredient():
    ingredient = Ingredient(data.INGREDIENT_TYPE, data.INGREDIENT_NAME, data.INGREDIENT_PRICE)
    return ingredient


@pytest.fixture
def mock_bun():  # мок объекта класса булка
    mock_bun = Mock(Bun)
    mock_bun.return_value.get_name = data.BUN_NAME
    mock_bun.return_value.get_price = data.BUN_PRICE
    return mock_bun


@pytest.fixture
def mock_ingredient_sauce():  # мок игнредиента. используем в тестах бургера
    mock_ingredient_sauce = Mock(Ingredient)
    mock_ingredient_sauce.name = data.INGREDIENT_NAME
    mock_ingredient_sauce.price = data.INGREDIENT_PRICE
    mock_ingredient_sauce.ingredient_type = INGREDIENT_TYPE_SAUCE
    mock_ingredient_sauce.return_value.get_name = data.INGREDIENT_NAME
    mock_ingredient_sauce.return_value.get_price = data.INGREDIENT_PRICE
    mock_ingredient_sauce.return_value.get_type = data.INGREDIENT_TYPE
    return mock_ingredient_sauce


@pytest.fixture
def mock_ingredient_filling():  # мок игнредиента. используем в тестах бургера
    mock_ingredient_filling = Mock(Ingredient)
    mock_ingredient_filling.name = data.INGREDIENT_NAME_FILLING
    mock_ingredient_filling.price = data.INGREDIENT_PRICE_FILLING
    mock_ingredient_filling.ingredient_type = INGREDIENT_TYPE_FILLING
    mock_ingredient_filling.return_value.get_name = data.INGREDIENT_NAME_FILLING
    mock_ingredient_filling.return_value.get_price = data.INGREDIENT_PRICE_FILLING
    mock_ingredient_filling.return_value.get_type = data.INGREDIENT_TYPE_FILLING
    return mock_ingredient_filling


@pytest.fixture()
def burger_test(mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
    burger_test = Burger()
    burger_test.set_buns(mock_bun)
    burger_test.add_ingredient(mock_ingredient_sauce)
    burger_test.add_ingredient(mock_ingredient_filling)
    return burger_test
