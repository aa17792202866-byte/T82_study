# 字典题：
# 1.  编写程序将列表s=[6,17,81,3,29,12,51,16]中能被3整除的数减2，其他数保持不变；用一个字典统计变化的数,和不变的数.
# s=[6,17,81,3,29,12,51,16]
# s1,s2 = [],[]
# d = {}
# for i in range(len(s)):
#     if s[i] % 3 == 0:
#         s1.append(s[i]-2)
#     else:
#         s2.append(s[i])
# d["变化的数"] = s1
# d["不变的数"] = s2
# print(d)


# 2.  将列表 [11,22,33,1,6,4,88,44]中元素分成大于33的部分,和小于33的部分,用一个字典来表示划分结果
# s = [11,22,33,1,6,4,88,44]
# s1,s2 = [],[]
# d = {}
# for i in range(len(s)):
#     if s[i] >= 33:
#         s1.append(s[i])
#     else:
#         s2.append(s[i])
# d["大于33的数字"] = s1
# d["小于33的数字"] = s2
# print(d)

# 3.  用户随机输入N个大写字母,程序使用dict统计用户输入的每个字母的次数 (字典题)
#存在问题，只能一个一个输入
# N = 10
# s = []
# d = {}
# for i in range(1,N+1): #让用户输入，N个数值
#     while 1:
#         a = input(f"请输入第{i}个大写字母(共{N}个)：")
#         if len(a) == 1 and a.isupper(): #确保用户输入的为单个大写字母
#             s.append(a)
#             break
#         else:
#             print("请输入单个大写字母")
# for i in s: #遍历用户输入的所有字母的列表
#     if i not in d: #判断字母是不是已经加入了字典，防止重复
#         cishu = s.count(i) #统计未加入字典的首次出现的字母位于列表中出现的数量
#         d[i+"输入的数量"] = cishu #将次数添加进入字典，字母作为键，次数作为值
# print(d)



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

# 4.  设定记录用户名和密码的列表为
#      user_info = [{’username’:’admin’,’password’:’123456’},{’username’:’test1’,’password’:’t123456’},
#                        {’username’:’sgn1’,’password’:’s123456’}]
#     允许用户输入三次用户名和密码,输入正确提示用户登录成功,结束循环,如果输入不正确,提示用户"用户名或密码错误".
#     如果三次不成功,需要锁定账号,提示用户:"由于输入错误次数太多,您的账号已被锁定!"

# user_info = [{'username':'admin','password':'123456'},{'username':'test1','password':'t123456'},{'username':'sgn1','password':'s123456'}]
# num1 = 0 #定义一个可以判断是否处于输入成功状态的变量
# for i in range(1,4):
#     name = input("请输入用户名：")
#     password = input("请输入密码：")
#     for item in user_info: #遍历这个字典
#         if item["username"] == name and item["password"] == password: #验证输入的和字典的键值以及value是不是相同
#             num1 += 1 #输入成功，这个num1可以让其能跳出第二层循环
#             break
#     if num1:
#         print("登陆成功")
#         break
#     else:
#         print(f"用户名或密码错误,您还有{3-i}次机会")
# else:
#     print("由于输入错误次数太多,您的账号已被锁定!")

# 5. 定义一个电话簿，里头设置以下联系人：
# 'mayun':'13309283335',
# 'zhaolong':'18989227822',
# 'zhangmin':'13382398921',
# 'Gorge':'19833824743',
# 'Jordan':'18807317878',
# 'Curry':'15093488129',
# 'Wade':'19282937665'
#     现在输入人名，查询他的号码(要求：实现模糊查询：用户输入姓名的部分信息，就可查找到对应的完整姓名及手机号）。

# telephone1 = {'mayun':'13309283335','zhaolong':'18989227822','zhangmin':'13382398921','Gorge':'19833824743','Jordan':'18807317878','Curry':'15093488129','Wade':'19282937665'}
# name = input("请输入人名")
# result = {}
# sum5 = 0
# for k,v in telephone1.items():
#     if name in k:
#         result[k] = v
#         sum5 += 1
# if not sum5:
#     print(f"未找到{name}对应的电话")
# else:
#     print(result)

# 6.  有一个字典保存英文单词和它的译文,例:{'hello':'你好','world':'世界'},
#      输入某个单词,查看它的译文,如果没有,就提示用户,并将该单词和译文加入字典,如果有,输出译文.
# d = {'hello':'你好','world':'世界'}
# danci = input("请输入单词")
# for k,v in d.items():
#     if danci == k:
#         print(f"{k}的译文为{v}")
#         break
# else:
#     danci1 = input("请输入该单词(将该单词加入字典)")
#     yiwen1 = input("请输入该单词的译文(将该译文加入字典)")
#     d[danci1] = yiwen1
#     print(d)

# 7.  给定n个整数的列表，请统计出每个整数出现的次数，按出现次数从多到少的顺序输出,输出为字典。
#      list = [3,4,1,2,5,6,7,1,2,3,7,2,6,8,9,0,1,4,7,9,2,3,7,9,1]
#      dict ={4: [1, 2, 7], 3: [3, 9], 2: [4, 6], 1: [5, 8, 0]}

"""失败了的
list7 = [3,4,1,2,5,6,7,1,2,3,7,2,6,8,9,0,1,4,7,9,2,3,7,9,1]
result = []
dict = {}
for num in list7:

    if num not in result:
        cishu = list7.count(num) #将该数字出现的次数计算出来
        for i in list7:
            if list7.count(i) == cishu: #如果其他数字出现的次数和第一个遇见的这个数字的次数一致，将它们存入一个列表中
                result.append(i)
        print(result)
        # dict[cishu] = num
"""

# list7 = [3,4,1,2,5,6,7,1,2,3,7,2,6,8,9,0,1,4,7,9,2,3,7,9,1]
# result = {}
# for num in list7:
#     cishu = list7.count(num) # 统计当前数字 num 在整个列表中出现了多少次
#     if cishu not in result:  # 判断这个“出现次数”是否已经作为字典的键存在,如果不存在，就先创建一个空列表
#         result[cishu] = []
#     if num not in result[cishu]: # 判断当前数字 num 是否已经保存到对应次数的列表中,防止同一个数字被重复添加
#         result[cishu].append(num)  # 把当前数字添加到对应次数的列表中
# result1 = dict(sorted(result.items(),reverse=True)) #逆序排列
# print(result1)

list7 = [3, 4, 1, 2, 5, 6, 7, 1, 2, 3, 7, 2, 6, 8, 9, 0, 1, 4, 7, 9, 2, 3, 7, 9, 1]

# # 1. 统计每个数字出现的次数
# counts = {}
# for num in list7:
#     counts[num] = counts.get(num, 0) + 1
# # 2. 按出现次数分类，整理成 {次数: [数字列表]}
# result_dict = {}
# for num, cishu in counts.items():
#     if cishu not in result_dict:
#         result_dict[cishu] = []
#     result_dict[cishu].append(num)
# # 3. 按出现次数从大到小排序输出
# sorted_result = dict(sorted(result_dict.items(), key=lambda x: x[0], reverse=True))
# print(sorted_result)

# 8.  一年一度的校园好声音进行到了激烈的决赛环节，8位评委对入围的6名选手依次给出最终的评分，（用字典实现）
#   01.请写程序记录评委的打分.
#      提示：打分结果用字典表示，比如：fenshu = {1:[],2:[],3:[],4:[],5:[],6:[]}
#   02.请根据评分表，将每位选手的得分去掉一个最高分和一个最低分后求平均分,并打印每名选手的平均分
#   03.按照平均分由高到低的顺序输出选手编号和最后得分。
fenshu = {1:[1,2,3,4,5,6,7,8],2:[2,2,3,4,5,6,7,8],3:[3,2,3,4,5,6,7,8],4:[4,2,3,4,5,6,7,8],5:[5,2,3,4,5,6,7,8],6:[6,2,3,4,5,6,7,8]}
import random
biaoge = {1:[],2:[],3:[],4:[],5:[],6:[]}
result8 = {}
for i in biaoge: # 遍历6个选手
    for j in range(1, 9): # 每个选手由8个评委打分
        a = random.randint(1, 10) # 随机生成1~10分
        biaoge[i].append(a) # 把分数加入当前选手对应的列表
    print(i, biaoge[i]) # 输出当前选手的8个分数

for num,scores in fenshu.items():
    # 去掉最高分和最低分
    scores.remove(max(scores))
    scores.remove(min(scores))
    avg = sum(scores) / len(scores) # 计算平均分
    # print(f"选手 {num} 的平均分为: {avg:.2f}")
    fenshu[num] = round(avg,2)

# result8 = dict(sorted(fenshu.items(),reverse=True)) #写错了，这个是按照编号倒序排序，不是平均分
#使用lambda
result8 = dict(sorted(fenshu.items(), key=lambda x: x[1], reverse=True))
print(result8)
#冒泡排序
items = list(fenshu.items())
for i in range(len(items) - 1):
    for j in range(len(items) - 1 - i):
        if items[j][1] < items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]
result8 = dict(items)
print(result8)




