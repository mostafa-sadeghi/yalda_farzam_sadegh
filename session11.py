# mylist = []
# mylist.append("artin")
# mylist.append("armin")
# mylist.append("arshin")


# print(mylist)

# mylist.remove("artin")

# print(mylist)


# students = []
# for i in range(4):
#     new_name = input("enter a name: ")
#     students.append(new_name)


# print(students)

# TODO   همین کار را با حلقه وایل انجام دهید
# all_numbers = []
# for i in range(4):
#     new_number = int(input("enter a number: "))
#     all_numbers.append(new_number)
# print(all_numbers)
# print(sum(all_numbers))

# TODO
"""
برنامه بالا را به گونه ای تغییر دهید که تنها جمع اعداد فرد را محاسبه کند
"""


numbers = [1,2,3,4,5,6,7,8,9]
print(sum(numbers))

total = 0
for i in range(len(numbers)):
    total += numbers[i]
print(total)


numbers = [1,2,3,4,5,6,7,8,9]
print(numbers[:3])
print(numbers[3:6])


# TODO  "برش های زیر را از لیست ایجاد نمائید
#  [2,3,4]
#  [3,4]
#  [7,8,9]
#  [6,7,8]