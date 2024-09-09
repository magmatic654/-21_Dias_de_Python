# En este desafío, debes construir una lista de contactos mediante una hash table.
# Tu objetivo será implementar la lógica de la clase ContactList para agregar contactos y realizar las operaciones correspondientes.
# La hash table (ContactList) deberá tener los siguientes métodos:

# insert(name, phone): este método recibirá el nombre y el número de teléfono de un contacto y agregará este último a la hash table.

# get(name): este método recibirá el nombre de un contacto y devolverá su número de teléfono. Si el contacto no existe, retornará None.

# retrieveAll(): este método devolverá una lista con todos los buckets utilizados en la hash table.

# delete(name): este método recibirá el nombre de un contacto y eliminará dicho contacto de la hash table. En caso de no encontrar el nombre, debe retornar None.

# El código original ya tiene una implementación del método hash, por lo que no tienes que preocuparte por ello.

# Ejemplo 1:
# Input
# contactList = ContactList(10)
# contactList.insert("Mr michi", "123-456-7890")
# contactList.retrieveAll()
# Output: [["Mr michi", "123-456-7890"]]

# Ejemplo 2:
# Input:
# contactList = ContactList(10)
# contactList.insert("Mr michi", "123-456-7890")
# contactList.get("Mr Michi")
# Output: "123-456-7890"

# Ejemplo 3:
# Input:
# contactList = ContactList(10)
# contactList.insert("Mr michi", "123-456-7890")
# contactList.delete("Mr michi")
# contactList.get("Mr Michi")
# Output: None

class ContactList:
  def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]

  def hash(self, key):
        return hash(key) % self.size

  def insert(self, name, phone):
        index = self.hash(name)
        self.buckets[index].append((name, phone))

  def get(self, name):
        index = self.hash(name)
        for k, v in self.buckets[index]:
            if k == name:
                return v
        return None

  def retrieveAll(self):
    all_values = []
    for bucket in self.buckets:
        for k, v in bucket:
            all_values.append([k, v])
    return all_values

  def delete(self, name):
    index = self.hash(name)
    for i, (k, v) in enumerate(self.buckets[index]):
        if k == name:
            del self.buckets[index][i]
            return

contactList = ContactList(10)
contactList.insert("Mr Michi", "123-456-7890")
print(contactList.get("Mr Michi"))