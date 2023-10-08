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


def get_hours_minutes_seconds(total_seconds):
    if total_seconds >= 3600:
        hours = total_seconds // 3600
        total_seconds = total_seconds % 3600
    else:
        hours = 0
    if total_seconds >= 60:
        minutes = total_seconds // 60
        total_seconds = total_seconds % 60
    else:
        minutes = 0

    seconds = total_seconds
    return f'{hours}h:{minutes}m:{seconds}s'


print(get_hours_minutes_seconds(90))
print(get_hours_minutes_seconds(3601))

# TODO
"""
[28,25,42,2,28]    تابعی بنویسید که کوچکترین عدد را از این لیست به ما بدهد
[28,25,42,2,28]    تابعی بنویسید که بزرگترین عدد را از این لیست به ما بدهد
"""
