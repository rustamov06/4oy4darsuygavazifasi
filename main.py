# class LowercaseDescriptor:
#     def __init__(self):
#         self._value = ""
#
#     def __get__(self, instance, owner):
#         return self._value
#
#     def __set__(self, instance, value):
#         if isinstance(value, str):
#             self._value = value.lower()
#         else:
#             raise ValueError("Qiymat faqat string bo'lishi kerak!")
#
#     def __delete__(self, instance):
#         del self._value
# class Person:
#     name = LowercaseDescriptor()
#     def __init__(self, name):
#         self.name = name
# class Product:
#     title = LowercaseDescriptor()
#
#     def __init__(self, title):
#         self.title = title
# p1 = Person("ALi")
# print(f"Person name: {p1.name}")
# p2 = Product("SOFA")
# print(f"Product title: {p2.title}")
# p1.name = "MuRzo"
# print(f"Updated Person name: {p1.name}")
#
# # 2 vazifa
#
# class PositiveValueDescriptor:
#     def __init__(self):
#         self._value = 0
#     def __get__(self, instance, owner):
#         return self._value
#
#     def __set__(self, instance, value):
#         if isinstance(value, (int, float)) and value > 0:
#             self._value = value  # Musbat qiymat o'rnatiladi
#         else:
#             raise ValueError("Qiymat musbat son bo'lishi kerak!")
#     def __delete__(self, instance):
#         del self._value
# class BankAccount:
#     balance = PositiveValueDescriptor()
#     def __init__(self, balance):
#         self.balance = balance
# class Product:
#     price = PositiveValueDescriptor()
#     def __init__(self, price):
#         self.price = price
# try:
#     account = BankAccount(100)
#     print(f"Account balance: {account.balance}")
#     account.balance = 200
#     print(f"Updated balance: {account.balance}")
#     account.balance = -50
# except ValueError as e:
#     print(e)
# try:
#     product = Product(50)
#     print(f"Product price: {product.price}")
#     product.price = 0
# except ValueError as e:
#     print(e)



# # Datetime Moduli
# # 1 vazifa
#
# from datetime import datetime, timedelta
# bugungi_sana = datetime.now()
# sana_7_kun_oldin = bugungi_sana - timedelta(days=7)
# sana_7_kun_keyin = bugungi_sana + timedelta(days=7)
# print("Bugungi sana:", bugungi_sana.strftime('%Y-%m-%d'))
# print("7 kun oldingi sana:", sana_7_kun_oldin.strftime('%Y-%m-%d'))
# print("7 kun keyingi sana:", sana_7_kun_keyin.strftime('%Y-%m-%d'))

# 2 vazifa

# from datetime import datetime
# tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting (YYYY formatda): "))
# tugilgan_oy = int(input("Tug'ilgan oyingizni kiriting (1-12 orasida): "))
# tugilgan_kun = int(input("Tug'ilgan kuningizni kiriting: "))
# bugungi_sana = datetime.now()
# tugilgan_sana = datetime(tugilgan_yil, tugilgan_oy, tugilgan_kun)
# yosh = bugungi_sana.year - tugilgan_sana.year
# if (bugungi_sana.month, bugungi_sana.day) == (tugilgan_sana.month, tugilgan_sana.day):
#     print("Tug'ilgan kuningiz bilan!")
# else:
#     print(f"Sizning yoshingiz: {yosh} yosh.")

# 3 vazifa
#
# from datetime import datetime
# boshlanish_vaqti = input("Boshlanish vaqtini kiriting (hh:mm:ss formatda): ")
# tugash_vaqti = input("Tugash vaqtini kiriting (hh:mm:ss formatda): ")
# bugungi_sana = datetime.now()
# boshlanish_vaqt = datetime.strptime(boshlanish_vaqti, '%H:%M:%S')
# tugash_vaqt = datetime.strptime(tugash_vaqti, '%H:%M:%S')
# boshlanish_vaqt = bugungi_sana.replace(hour=boshlanish_vaqt.hour, minute=boshlanish_vaqt.minute, second=boshlanish_vaqt.second)
# tugash_vaqt = bugungi_sana.replace(hour=tugash_vaqt.hour, minute=tugash_vaqt.minute, second=tugash_vaqt.second)
#
# if tugash_vaqt < boshlanish_vaqt:
#     tugash_vaqt = tugash_vaqt.replace(day=bugungi_sana.day + 1)
# vaqt_oraligi = tugash_vaqt - boshlanish_vaqt
# soniyalar = vaqt_oraligi.total_seconds()
# print(f"Boshlanish va tugash vaqti orasidagi jami soniyalar: {int(soniyalar)} soniya.")


# Math Moduli
# 1 vazifa

# import math
# diametr = float(input("Aylananing diametrini kiriting: "))
# radius = diametr / 2
# yuzasi = math.pi * (radius ** 2)
# print(f"Aylana yuzasi: {yuzasi:.2f}")

# 2 vazifa

# import math
#
# try:
#     son = float(input("Sonni kiriting: "))
#     if son < 0:
#         raise ValueError("Manfiy son uchun ildizlar mavjud emas!")
#     kvadrat_ildiz = math.sqrt(son)
#     kub_ildiz = son ** (1 / 3)
#     print(f"Sonning kvadrat ildizi: {kvadrat_ildiz:.2f}")
#     print(f"Sonning kub ildizi: {kub_ildiz:.2f}")
# except ValueError as e:
#     print(f"Hatolik: {e}")
