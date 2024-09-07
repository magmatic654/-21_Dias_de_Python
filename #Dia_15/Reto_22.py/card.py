from pay import Pay

class Card(Pay):
    def __init__(self, card_numbers):
        self._card_numbers = card_numbers

    @property
    def card_numbers(self):
        return self._card_numbers
    
    @card_numbers.setter
    def card_numbers(self, new_card_numbers):
        self._card_numbers == new_card_numbers
    
    def make_pay(self, quantity):
        if len(str(self._card_numbers)) != 16:
            raise Exception('La tarjeta de credito no es de 16 digitos')
        info = super().make_pay(quantity)
        last_card_numbers = str(self._card_numbers)[-4:]
        info['last_card_numbers'] = last_card_numbers
        return info
    
if __name__ == '__main__':
    card = Card(1234567812345678)
    print(card.make_pay(1000))