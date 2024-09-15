
class TestIngredient:
    def test_ingredient_get_name(self, ingredient):
        ingredient_name = ingredient.get_name()
        assert ingredient_name == ingredient.name
        print(f'ожидаемое имя ингредиента: {ingredient.name}')

    def test_ingredient_get_price(self, ingredient):
        ingredient_price = ingredient.get_price()
        assert ingredient_price == ingredient.price
        print(f'ожидаемая цена ингредиента: {ingredient.price}')

    def test_ingredient_get_type(self, ingredient):
        ingredient_type = ingredient.get_type()
        assert ingredient_type == ingredient.type
        print(f'ожидаемое имя ингредиента: {ingredient.type}, фактическое: {ingredient_type}')
