from pay import Pay

class PayPal(Pay):
    def __init__(self, email):
        self._email = email
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        self._email = new_email

    def make_pay(self, quantity):
        info = super().make_pay(quantity)
        info['email'] = self._email
        info['platform'] = 'PayPal'
        return info
    
if __name__ == '__main__':
    user = PayPal('abc@mail.com')
    print(user.make_pay(2000))