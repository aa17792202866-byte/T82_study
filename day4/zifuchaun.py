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

s = "Hello"
for i in range(len(s)):
    print(i, s[i])

s = "Hello"
for index, char in enumerate(s):
    print(index, char)