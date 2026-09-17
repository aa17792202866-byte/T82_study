# a,b = 1,2
# print(a,b)
# a,b=b,a
# print(a,b)
# a,b = 1,2
# print(a,b)
# a,b=b,a
# print(a,b)
# s = input("请输入大写字母：")
# # 判断s是大写字母，则统计每个大写字母出现的次数；否则提示用户
# if s.isupper():
#     # 定义空字典
#     count_dict = {}
#     # 遍历输入字符串里的每一个字符
#     for char in s:
#         if char in count_dict:
#             # 如果字典已有该字母，次数+1
#             count_dict[char] += 1
#         else:
#             # 字典没有该字母，初始次数为1
#             count_dict[char] = 1
#     # 输出统计结果字典
#     print(count_dict)
# else:
#     print("输入的不是全大写字母！")

# result = {}
# while 1:
#     text = input("请输入一串大写字母：")  # 用户输入: AABBCDA
#     for char in text:
#         if char.isupper():  # 过滤非大写字母（可选）
#             result[char] = result.get(char, 0) + 1
#     if result:
#         break
#     else:
#         print("请输入大写字母字符串")
# print(result)


sheng = ("陕西","山西")
shi = ("西安","太原")
dict1 = {sheng[i]:shi[j] for i in range(len(sheng)) for j in range(len(shi)) if i == j}
print(dict1)

sheng = ('陕西', '山西', '河南')
shi = ('西安', '太原', '郑州')

# 正确写法：用 zip 函数同步打包
dict1 = {i: j for i, j in zip(sheng, shi)}

# 或者更直接（zip 结果可以直接转字典）
dict1 = dict(zip(sheng, shi))

print(dict1)
# 输出: {'陕西': '西安', '山西': '太原', '河南': '郑州'}