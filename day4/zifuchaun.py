# 1.从请求地址中提取出用户名和域名http://www.163.com?userName=admin&pwd=123456
# str1 = 'http://www.163.com?userName=admin&pwd=123456'
# sum1 = 0
# for i in str1:
#     print(i,end=" ")
#
#     print(f"{sum1}")
#     sum1 = sum1 + 1
# print(str1[28:33])
# print(str1[7:18])

# 2.根据完整路径从路径中分离文件路径，文件名及文件扩展名
# 注意python中一个反斜杠有特殊含义，所以要用二个反斜杠
# str2 = "D:\\软件\python\\python39\\Tools\scripts\\abitype.py"
# str2 = "D:\\软件\python\\python39\\Tools\scripts\\abitype.py"
# sum1 = 0
# for i in str2:
#     print(i,end=" ")
#
#     print(f"{sum1}")
#     sum1 = sum1 + 1
# print(str2[:])

# s = "Hello"
# for i in range(len(s)):
#     print(i, s[i])
#
# s = "Hello"
# for index, char in enumerate(s):
#     print(index, char)

# s = "abcdefghijklmnopq"
# print(s.find("cds"))

# s = "我"
# print(s.isalnum())

s = "abcdefsdsadabcsadabccabcczabczccabczxzabczxdaabcadabcabc"
# count = 0
# state = 0  # 记录当前匹配到了第几个字符
#
# for char in s:
#     if state == 0 and char == "a":
#         state = 1
#     elif state == 1:
#         if char == "b":
#             state = 2
#         elif char == "a":
#             state = 1
#         else:
#             state = 0
#     elif state == 2:
#         if char == "c":
#             count += 1
#             state = 0
#         elif char == "a":
#             state = 1
#         else:
#             state = 0
#
# print(count)  # 输出: 2
for i in range(len(s)):
    print(i,s[i])
print(s.rfind("a"))
print(s[53])