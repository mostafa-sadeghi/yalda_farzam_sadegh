# def find_color(x,y):
#     if x % 2 == y % 2:
#         return "white"
#     else:
#         return "black"

# print(find_color(1,1))
# print(find_color(1,2))
# print(find_color(1,5))
# print(find_color(5,5))
# print(find_color(6,5))
# print(find_color(4,4))


# message = "the fox is looking for another fox to join with that fox"
# # print(message.count("fox"))

# def my_count(m,w):
#     c = 0
#     for i in range(len(m)):
#         if m[i:i+len(w)] == w:
#             c += 1

#     return c


# print(my_count(message, "fox"))


"""
90              ->          1m:30s
30              ->          30s
60              ->          1m
3600            ->          1h
3601            ->          1h1s
"""


# def get_hours_minutes_seconds(total_seconds):
#     if total_seconds >= 3600:
#         hours = total_seconds // 3600
#         total_seconds = total_seconds % 3600
#     else:
#         hours = 0
#     if total_seconds >= 60:
#         minutes = total_seconds // 60
#         total_seconds = total_seconds % 60
#     else:
#         minutes = 0

#     seconds = total_seconds
#     return f'{hours}h:{minutes}m:{seconds}s'


# print(get_hours_minutes_seconds(90))
# print(get_hours_minutes_seconds(3601))

# TODO
"""
[28,25,42,2,28]    تابعی بنویسید که کوچکترین عدد را از این لیست به ما بدهد
[28,25,42,2,28]    تابعی بنویسید که بزرگترین عدد را از این لیست به ما بدهد
"""


# def get_min(x):
#     smallest = x[0]
#     for number in x:
#         if number < smallest:
#             smallest = number
#     return smallest
# print(get_min([28, 25, 42, 2, 28]))


# def get_max(x):
#     largets = x[0]
#     for number in x:
#         if number > largets:
#             largets = number
#     return largets
# print(get_max([28, 25, 42, 2, 28]))


# def get_color(x, y):
#     if x % 2 == y % 2:
#         return "white"
#     else:
#         return "black"


# print(get_color(1, 1))
# print(get_color(2, 2))
# print(get_color(2, 3))
# print(get_color(2, 6))


# import random
# def show_winner(move_1, move_2):
#     if move_1 == "rock" and move_2 == "paper":
#         return "player 2 is winner"
#     elif (move_1 == "rock" and move_2 == "scissors"):
#         return "player 1 is winner"
#     elif move_1 == "paper" and move_2 == "scissors":
#         return "player 2 is winner"
#     elif move_1 == "paper" and move_2 == "rock":
#         return "player 1 is winner"
#     elif move_1 == "scissors" and move_2 == "rock":
#         return "player 2 is winner"
#     elif move_1 == "scissors" and move_2 == "paper":
#         return "player 1 is winner"
#     else:
#         return "equal"


# all_options = ("rock", "paper", "scissors")

# print(show_winner(random.choice(all_options), random.choice(all_options)))
# print(show_winner("rock", "paper"))
# print(show_winner("scissors", "paper"))
# print(show_winner("rock", "scissors"))
# print(show_winner("rock", "rock"))


"""

تابعی بنویسید که نمرات سه درس یک دانش آموز را دریافت نماید
معدل او را محاسبه کند
اگر معدل او از 90 بیشتر بود
A
اگر معدل او از 80 بیشتر بود
B
اگر معدل او از 70 بیشتر بود
C
اگر معدل او از 60 بیشتر بود
D
اگر معدل او از 50 بیشتر بود
E
در غیر اینصورت 
F
را نمایش بده

"""
