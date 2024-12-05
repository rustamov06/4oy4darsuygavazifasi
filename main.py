class LowercaseDescriptor:
    def __init__(self):
        self._value = ""

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if isinstance(value, str):
            self._value = value.lower()
        else:
            raise ValueError("Qiymat faqat string bo'lishi kerak!")

    def __delete__(self, instance):
        del self._value
class Person:
    name = LowercaseDescriptor()
    def __init__(self, name):
        self.name = name
class Product:
    title = LowercaseDescriptor()

    def __init__(self, title):
        self.title = title
p1 = Person("ALi")
print(f"Person name: {p1.name}")
p2 = Product("SOFA")
print(f"Product title: {p2.title}")
p1.name = "MuRzo"
print(f"Updated Person name: {p1.name}")

# 2 vazifa

class PositiveValueDescriptor:
    def __init__(self):
        self._value = 0
    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if isinstance(value, (int, float)) and value > 0:
            self._value = value  # Musbat qiymat o'rnatiladi
        else:
            raise ValueError("Qiymat musbat son bo'lishi kerak!")
    def __delete__(self, instance):
        del self._value
class BankAccount:
    balance = PositiveValueDescriptor()
    def __init__(self, balance):
        self.balance = balance
class Product:
    price = PositiveValueDescriptor()
    def __init__(self, price):
        self.price = price
try:
    account = BankAccount(100)
    print(f"Account balance: {account.balance}")
    account.balance = 200
    print(f"Updated balance: {account.balance}")
    account.balance = -50
except ValueError as e:
    print(e)
try:
    product = Product(50)
    print(f"Product price: {product.price}")
    product.price = 0
except ValueError as e:
    print(e)

