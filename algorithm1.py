# def even_or_odd(number):
#     if number % 2 == 0:
#         return f'{number} is even'
#     else:
#         return f'{number} is odd'

# print(even_or_odd(13))
# print(even_or_odd(14))

# def area(x, y):
#     return x * y


# print(area(4, 2))


# def perimeter(x, y):
#     return 2*(x+y)


# print(perimeter(4, 2))


"""
0   =>  0th
1   =>  1st
2   =>  2nd
3   =>  3rd
11  =>  11th
12  =>  12th
13  =>  13th

4   =>  4th

123 => 123rd
511 => 511th
55  => 55th
"""


def my_function(number):
    if number % 100 in (11, 12, 13):
        return str(number) + "th"
    elif number % 10 == 0:
        return str(number)+"th"
    elif number % 10 == 1:
        return str(number) + "st"
    elif number % 10 == 2:
        return str(number) + "nd"
    elif number % 10 == 3:
        return str(number) + "rd"
    else:
        return str(number)+"th"
print(my_function(1))
print(my_function(2))
print(my_function(3))
print(my_function(4))
print(my_function(411))
print(my_function(412))
print(my_function(4311))