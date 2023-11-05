# numbers = (1, 2, 3, 33, 400, 8, 14, 24)

# for number in numbers:
#     if number % 2 == 0 and number != 2:
#         print(number)

# همه اعداد زوجی که رقم دو ندارند


# numbers = (1, 2, 3, 33, 400, 8, 14, 24)
# for number in numbers:
#     if number % 2 == 0:
#         if "2" not in str(number):
#             print(number)

# TODO
message = "salaam khobi?"
# با کمک حلقه فور تک تک کاراکترهای متن بالا را نمایش دهید
# با کمک حلقه وایل تک تک کاراکترهای متن بالا را نمایش دهید
# با کمک حلقه فور تک تک کاراکترهای انگلیسی متن بالا را نمایش دهید

# for x in message:
#     print(x)

# i = 0
# while i < len(message):
#     print(message[i])
#     i += 1

for x in message:
    if x != " " and x != "?":
        print(x)


message = """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Id quod odit similique! Repudiandae, perspiciatis suscipit, officiis exercitationem laudantium nihil magnam hic et tempore mollitia quibusdam, quos officia. Vero, veniam libero!
"""
import string
white_list =string.ascii_letters
print(white_list)
for x in message:
    if x in white_list:
        print(x)