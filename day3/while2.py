# 登录脚本:
# 需要用户输入用户名和密码,内定:admin, 123456,
# 允许用户输入三次,输入正确提示用户,登录成功,结束循环,如果输入不正确,提示用户"用户名或密码错误".
# 如果三次不成功,需要锁定账号,提示用户:"由于输入错误次数太多,您的账号已被锁定!"

i = 1
while i <= 3:
    user_name = input("请输入用户名")
    user_password = input("请输入密码")
    if user_name == 'admin' and user_password == '123456':
        print("登陆成功")
        break
    elif i < 3:
        print("用户名或密码错误")
    else:
        print("由于输入错误次数太多,您的账号已被锁定!")
    i += 1


# i = 1
# while i <= 3:
#     user_name = input("请输入用户名")
#     user_password = input("请输入密码")
#     if user_name == 'admin' and user_password == '123456':
#         print("登陆成功")
#         break
#     else:
#         print("用户名或密码错误")
#     if i == 3:
#         print("由于输入错误次数太多,您的账号已被锁定!")
#     i += 1
