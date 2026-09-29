# import re
#
# s = "abc123XYZ"
#
# result = re.findall(r"[a-zA-Z]", s)
#
# print(result)
# 练习1: 写正则，判断输入的是否为手机号？

import re
# phone = input("Enter your phone number: ")
# if re.findall("1",phone[0]) and re.findall("[3-9]",phone[1]) and len(re.findall("[0-9]",phone[2:12]))==9:
#     print("是一个手机号")
# else:
#     print("不是一个手机号")

# 练习2：写正则，判断用户输入的密码是否符合规则: 6-16位,大小写数字和_混合？
password = input("Enter your password: ")
if 6 <= len(password) <= 16 and re.findall("[a-zA-Z0-9]",password) and re.findall("[_]",password):
    print("是大小写数字_混合")
else:
    print("不是混合")
    