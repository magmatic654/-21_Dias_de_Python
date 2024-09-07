from paypal import PayPal
from card import Card
from cash import Cash

def process_pay(method, quantity):
    return method.make_pay(quantity)

if __name__ == '__main__':
    paypal = PayPal("test@mail.com")
    print(process_pay(paypal, 240))