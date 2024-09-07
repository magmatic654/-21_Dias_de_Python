from pay import Pay

class Cash(Pay):
    pass

if __name__ == '__main__':
    cash = Cash()
    print(cash.make_pay(1000))