import pytest
import data
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns(self, bun):  # булка
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun.name == data.BUN_NAME
        print(f' Получаем имя булки при методом set_bun : {burger.bun.name}, Ожидаемый результат: {data.BUN_NAME}')

    def test_set_two_buns(self, bun):
        burger1 = Burger()
        burger2 = Burger()
        burger1.set_buns(bun)
        burger2.set_buns(bun)
        assert burger1.bun.name == data.BUN_NAME and burger2.bun.name == data.BUN_NAME
        print(f'{burger1.bun.name}, {burger2.bun.name}')

    def test_add_two_ingredient_sauces_and_fillings(self, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == 2
        print(f'Ожидаемое кол-во ингредиентов в бургере: {len(burger.ingredients)}, \n'
              f'ингредиент с индексом 0: {burger.ingredients[0].name},\n'
              f'ингредиент с индексом 1: {burger.ingredients[1].name}')

    @pytest.mark.parametrize('ingredient_var', [
        'mock_ingredient_sauce',
        'mock_ingredient_filling']
                             )
    def test_add_one_ingredient_sauces_or_fillings(self, ingredient_var):
        burger = Burger()
        burger.add_ingredient(ingredient_var)
        assert len(burger.ingredients) == 1
        print(f'Ожидаемое кол-во ингредиентов в бургере: {len(burger.ingredients)}')

    @pytest.mark.parametrize('index', [0, 1])
    def test_remove_ingredients_param_sauces_or_fillings(self, burger_test, index):
        burger_test.remove_ingredient(index)
        assert len(burger_test.ingredients) == 1  # в бургере два ингредиента, удаляем один
        print(f'Ожидаемое кол-во ингредиентов в бургере: {len(burger_test.ingredients)}')

    def test_remove_ingredient_from_empty_list(self, burger_test):
        burger_test.remove_ingredient(0)
        burger_test.remove_ingredient(0)
        assert len(burger_test.ingredients) == 0
        print(f'Ожидаемое кол-во ингредиентов в бургере: {len(burger_test.ingredients)}')

    def test_move_ingredients_sauces_and_fillings(self, burger_test):
        print(f'До перемещения ингредиент с индексом 0: {burger_test.ingredients[0].name}, с индексом 1: '
              f':{burger_test.ingredients[1].name}')
        burger_test.move_ingredient(0, 1)
        assert (burger_test.ingredients[1].name == data.INGREDIENT_NAME and burger_test.ingredients[0].name ==
                data.INGREDIENT_NAME_FILLING)
        print(f'После перемещения ингредиент с индексом 0: {burger_test.ingredients[0].name}, с индексом 1: '
              f':{burger_test.ingredients[1].name}')

    def test_move_ingredients_without_changing_index(self, burger_test):
        print(f'До перемещения ингредиент с индексом 1: {burger_test.ingredients[1].name}')
        burger_test.move_ingredient(1, 1)
        assert burger_test.ingredients[1].name == data.INGREDIENT_NAME_FILLING
        print(f'После перемещения:{burger_test.ingredients[1].name}')

    def test_move_ingredients_in_empty_list_index_error(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.move_ingredient(1, 0)
        assert len(burger.ingredients) == 0, f'{IndexError}'
        print(f'Невозможно поменять местами ингредиенты если список пустой:{burger.ingredients} класс ошибки:'
              f' {IndexError}')

    def test_empty_burger(self, bun):
        burger = Burger()
        assert len(burger.ingredients) == 0 and burger.bun == None

    def test_get_price_buns_ingredients(self, bun, ingredient):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        burger.get_price()
        assert burger.get_price() == bun.get_price() * 2 + ingredient.get_price()

    def test_get_receipt_buns_ingredients(self, bun, ingredient):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        burger.get_receipt()
        assert 'Price' and data.BUN_NAME in burger.get_receipt()
        print(f'{burger.get_receipt()}')

    def test_get_receipt_empty_burger(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_receipt()
        assert len(burger.ingredients) == 0

    def test_get_receipt_only_buns(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        burger.get_receipt()
        assert 'Price' and data.BUN_NAME in burger.get_receipt()
        print(f'{burger.get_receipt()}')