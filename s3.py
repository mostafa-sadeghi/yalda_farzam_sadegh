# name = input('What is your name? ')
# family = input('What is your family? ')

# print("hello", name, family)


# number1 = int(input('Enter first number: '))
# number2 = int(input('Enter second number: '))

# print(number1 + number2)

# number1 = float(input('Enter first number: '))
# number2 = float(input('Enter second number: '))

# print(number1 + number2)

# تمرین:
# برنامه ای بنویسید که دو عدد صحیح را از ورودی دریافت نماید
# و در هم ضرب نماید
# *
# و همینطور تقسیم و تفریق را نیز انجام دهید

# کارهای بالا را برای دو عدد اعشاری انجام دهید


# number1 = int(input('Enter a number: '))
# number2 = int(input('Enter a number: '))
# print("number1 + number2 =", number1 + number2)
# print(f"{number1} + {number2} =", number1 + number2)
# print("number1 - number2 =", number1 - number2)
# به عنوان تمرین برای بقیه هم انجام دهید
# print("number1 * number2 =", number1 * number2)
# print("number1 / number2 =", number1 / number2)
# print("number1 / number2 =", number1 // number2)


# a = 4
# b = 5

# print(a > b) # بزرگتری
# print(a < b) # کوچکتری
# print(a == b) # مساوی
# print(a != b) # نامساوی
# print(a >= b) # بزرگتر یا مساوی
# print(a <= b) # کوچکتر یا مساوی

# if a < b:
#     print("a is less than b")
#     print("ok")

# print("outside")

# if a > b:
#     print("a is greater than b")
# TODO
# تمرین:
# برنامه ای بنویسید که دو عدد از ورودی دریافت نماید و با هم مقایسه کند
# نتیجه مقایسه را نیز بنویسید


number1 = float(input('Enter a number: '))
number2 = float(input('Enter a number: '))

# print(number1 == number2)
# print(number1 >= number2)
# print(number1 <= number2)
# print(number1 != number2)
# print(number1 > number2)
# print(number1 < number2)

if number1 == number2:
    print(f"{number1} = {number2}")
elif number1 >= number2:
    print(f"{number1} >= {number2}")

# TODO
# برای بقیه هم انجام دهید

# a = 1

# if a == 1:
#     print("a = 1")


# a = 1
# b = 2
# c = 3

# if a < b and a < c:
#     print("a is less than b and c")


a = 1
b = 2
c = 0

if a < b and a < c:
    print("a is less than b and c")
