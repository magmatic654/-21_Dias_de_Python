class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def addToCart(self):
    raise NotImplementedError("La lógica de este método debe ser implementada por las clases hijas")

