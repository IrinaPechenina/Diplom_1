
class TestBun:

    #  проверка что можно получить имя булки
    def test_bun_get_name(self, bun):
        bun_name = bun.get_name()
        assert bun_name == bun.name
        print(f'ожидаемое имя булочки: {bun.name}')

    #  проверка что можно получить цену булки
    def test_bun_get_price(self, bun):
        bun_price = bun.get_price()
        assert bun_price == bun.price
        print(f'ожидаемая цена булочки: {bun.price}')
