user_name = input("enter the username: ")
password = input("enter the password: ")

all_users=[
    {'user_name':"ali", 'password':'123'},
    {'user_name':"nima", 'password':'nima123'},
    {'user_name':"artin", 'password':'12345'},
    {'user_name':"sara", 'password':'12345'},
    {'user_name':"samin", 'password':'s123'},
]
is_valid = False
for user in all_users:
    if user['user_name'] == user_name and user['password'] == password:
        print("login success!!!")
        print("secret key is:","SEC123")
        is_valid = True
        break

if is_valid == False:
    print("login was not successful")


# if user_name == "ali" and password == "123":
#     print("login success!!!")
#     print("secret key is:","SEC123")
# else:
#     print("login was not successful")


# import turtle

# turtle.goto(-100, 0)
# turtle.goto(100, 0)
# turtle.goto(0, 100)
# turtle.goto(-100, 0)

# turtle.done()



# for i in range(4):
#     color = turtle.textinput('color', "enter color name: ")
#     turtle.color(color)
#     turtle.right(90)
#     turtle.begin_fill()
#     for j in range(4):
#         turtle.fd(60)
#         turtle.left(90)
#     turtle.end_fill()
# turtle.done()