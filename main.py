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

