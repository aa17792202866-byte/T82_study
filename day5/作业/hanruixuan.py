# 理论题：
# 9.while循环的语法格式如何写？常见用于哪些场景下？
# while 条件:
#     循环体
# 常用于循环次数不确定、需要根据条件决定是否继续的场景，例如反复接收用户输入、菜单交互、重试操作。注意让条件有机会变为 False，或通过 break 退出，避免意外死循环。

# 10.range()函数的定义?开始值,结束值的取值范围?
# range() 返回一个表示整数序列的 range 对象，常用于控制循环次数。
# 开始值和结束值可以是正整数、负整数或 0。
# 步长可以为正数或负数，不能为 0。
# 正步长生成小于 stop 的值；负步长生成大于 stop 的值。方向不匹配时，序列为空，例如 range(5, 0)。

# 11.break和continue的区别?
# break:立即结束所在的最内层循环
# continue:跳过本轮剩余代码，继续最内层循环的下一轮

# 12.for循环的两种格式分别是什么？
# 1.直接遍历可迭代对象中的元素
# for 变量 in 可迭代对象:
#     循环体
# 2.配合 range() 遍历整数序列
# for 变量 in range(开始值, 结束值, 步长):
#     循环体

# 13.字符串的输入和输出函数分别是？各自的返回值?
# 输入函数:input()	返回值:返回用户输入的字符串，类型为 str
# 输出函数:print()	返回值:返回 None

# 14. 说说字符串的切片和索引格式？索引中-1代表什么含义?切片的逆序怎么表示?
# 索引：获取单个字符。
# 格式为：字符串[索引]
# 例如：s = "Python"
# s[0]   # 'P'，第一个字符
# s[1]   # 'y'，第二个字符
# s[-1]  # 'n'，最后一个字符
# s[-2]  # 'o'，倒数第二个字符
# 正向索引从 0 开始，负向索引从 -1 开始。-1 表示最后一个字符。
# 切片：获取一段字符串。
# 字符串[开始索引:结束索引:步长]
# 同样遵循包含开始位置，不包含结束位置的规则，步长默认为 1。
# s = "Python"
# s[1:4]   # 'yth'
# s[:3]    # 'Pyt'
# s[3:]    # 'hon'
# s[::2]   # 'Pto'
# s[::-1]  # 'nohtyP'，整个字符串逆序
# 注意：索引越界会报错；切片边界超出范围通常不会报错。字符串不可变，不能通过 s[0] = "p" 修改字符。

# 15.字符串有哪些常用的函数？
# | 函数或方法 | 作用 | 示例及结果 |
# |---|---|---|
# | `len(s)` | 获取字符串长度 | `len("hello")` → `5` |
# | `s.lower()` | 转小写 | `"AbC".lower()` → `"abc"` |
# | `s.upper()` | 转大写 | `"AbC".upper()` → `"ABC"` |
# | `s.strip()` | 去除两端空白字符 | `" hi ".strip()` → `"hi"` |
# | `s.lstrip()` | 去除左端空白字符 | `" hi ".lstrip()` → `"hi "` |
# | `s.rstrip()` | 去除右端空白字符 | `" hi ".rstrip()` → `" hi"` |
# | `s.replace(old, new)` | 替换子字符串 | `"a-b".replace("-", ":")` → `"a:b"` |
# | `s.split(sep)` | 按分隔符拆分为列表 | `"a,b".split(",")` → `["a", "b"]` |
# | `sep.join(items)` | 用分隔符连接字符串 | `"-".join(["a", "b"])` → `"a-b"` |
# | `s.find(sub)` | 返回首次出现的索引，找不到返回 `-1` | `"hello".find("l")` → `2` |
# | `s.index(sub)` | 返回首次出现的索引，找不到报错 | `"hello".index("e")` → `1` |
# | `s.count(sub)` | 统计子字符串出现次数 | `"hello".count("l")` → `2` |
# | `s.startswith(prefix)` | 判断是否以指定内容开头 | `"hello".startswith("he")` → `True` |
# | `s.endswith(suffix)` | 判断是否以指定内容结尾 | `"hello".endswith("lo")` → `True` |
# | `s.isdigit()` | 判断是否非空且全部为数字字符 | `"123".isdigit()` → `True` |
# | `s.isalpha()` | 判断是否非空且全部为字母字符 | `"abc".isalpha()` → `True` |
# | `s.isalnum()` | 判断是否非空且全部为字母或数字字符 | `"abc123".isalnum()` → `True` |
# 注意:字符串方法不会修改原字符串。需要保留处理结果时，应赋值：
# s = "hello"
# s = s.upper()
# print(s)  # HELLO
# 16. 说说列表的增删改查和遍历操作？
# ① 增加元素
# nums = [10, 20]
#
# nums.append(30)         # 末尾添加一个元素：[10, 20, 30]
# nums.extend([40, 50])   # 逐个追加多个元素：[10, 20, 30, 40, 50]
# nums.insert(1, 15)      # 在索引 1 处插入：[10, 15, 20, 30, 40, 50]
# append() 添加一个整体，extend() 逐个添加可迭代对象中的元素：
# a = [1, 2]
# a.append([3, 4])  # [1, 2, [3, 4]]
#
# b = [1, 2]
# b.extend([3, 4])  # [1, 2, 3, 4]
# ② 删除元素
# nums = [10, 20, 30, 20, 40]
#
# nums.remove(20)     # 删除第一个 20，剩余 [10, 30, 20, 40]
# last = nums.pop()  # 删除并返回最后一个元素，last 为 40
# first = nums.pop(0)  # 删除并返回索引 0 的元素，first 为 10
# del nums[0]        # 删除索引 0 的元素，剩余 [20]
# nums.clear()       # 清空列表，变为 []
# remove() 找不到指定值会报错；pop() 使用无效索引或对空列表操作会报错。
# ③ 修改元素
# nums = [10, 20, 30, 40]
#
# nums[1] = 99          # [10, 99, 30, 40]
# nums[1:3] = [7, 8]    # [10, 7, 8, 40]
# ④ 查询元素
# nums = [10, 20, 30, 20]
#
# nums[0]          # 10：按索引访问
# nums[-1]         # 20：访问最后一个元素
# nums[1:3]        # [20, 30]：切片
# 20 in nums       # True：判断是否存在
# 50 not in nums   # True：判断是否不存在
# nums.index(20)   # 1：查找第一次出现的位置，找不到报错
# nums.count(20)   # 2：统计出现次数
# len(nums)        # 4：获取元素数量
# ⑤ 遍历列表
# fruits = ["苹果", "香蕉", "橘子"]
#
# # 直接遍历元素
# for fruit in fruits:
#     print(fruit)
#
# # 按索引遍历
# for i in range(len(fruits)):
#     print(i, fruits[i])
#
# # 同时获取索引和元素
# for i, fruit in enumerate(fruits):
#     print(i, fruit)
#
# for i in range(len(fruits)):
#     print(i, fruits[i])
# 这里的enumerate(fruits)和range(len(fruits))是一样的效果，需要同时获取索引和元素时，enumerate() 更简洁。
# # 使用 while 遍历
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

#
# 列表题：
# 1. 求100-200以内同时能被7,8整除的数,保存在列表中.
# list1 = []
# for i in range(100,201):
#     if i % 7 == 0 and i % 8 == 0:
#         list1.append(i)
# print(list1)
# 2. 循环录入5个数字，用一个列表保存, 然后将该列表从小到大排序的结果和不排序但原列表逆序的结果分别保存在两个列表中.
# list2 = []
# for i in range(5):
#     num2 = input(f"请输入第{i+1}个数字")
#     list2.append(num2)
# list21 = sorted(list2)
# list22 = list2[::-1] #需要分别保存在两个列表中，所以采用“列表[::-1]”而不是“列表.reverse()”
# print(f"该列表从小到大排序的结果{list21}\n不排序但原列表逆序的结果{list22}")
# 3. 随机产生20个100-200之间的正整数存放到列表中，并求列表中的所有元素最大值、最小值、平均值，然后将各元素与平均值的差组成一个新列表。
# import random
# list3 = []
# list31 = []
# for i in range(1,21):
#     num3 = random.randint(100,200)
#     list3.append(num3)
# avg3 = sum(list3)/20 #计算列表平均数
# for i in list3:
#     list31.append(i-avg3) #将每个列表中的每个数字都减1，加入一个新列表中
# print(f"列表中的所有元素最大值{max(list3)}、最小值{min(list3)}、平均值{sum(list3)/20:.2f},各元素与平均值的差组成一个新列表为{list31}")

# 4. 找出一个列表中，只出现了2次的数字，并且保持原来的次序，例如[1,2,1,3,2,5]中只出现了2次的结果为[1,2]
# list4 = [1, 2, 1, 3, 2, 5,3,4,4]
# result = []
# for num in list4:
#     # 判断该数字在列表中出现了 2 次，且尚未加入结果列表
#     if list4.count(num) == 2 and num not in result:
#         result.append(num)
# print(result)  # 输出: [1, 2,3,4]

# 5. 编写程序将列表s=[6,17,81,3,29,12,51,16]中能被3整除的数减2，其他数保持不变,输出变换后的列表。
# s=[6,17,81,3,29,12,51,16]
# for i in range(len(s)): #使用含有索引值的遍历，为了方便进行替换列表值
#     if s[i] % 3 == 0:
#         s[i] = s[i] - 2 #将能被3整除的数字减去2，替换原来列表的数字
# print(s)
# 6.  ['12','13','33','34','1399','2315','1111']，移除这个数组中包含1的字符串（要求：直接在原列表上处理，不要将结果保存到新列表中）
# list6 = ['12','13','33','34','1399','2315','1111']
# for i in range(len(list6)-1,-1,-1):
#     if "1" in list6[i]:
#         list6.pop(i)    #第一种删除方法
#         # del(list6[i]) #第二种删除方法也可以
#         # list6.remove(list6[i]) #第三种删除方法也可以
# print(list6)
# 7.  移除一个列表中，数字小于33的元素  列表：[11,22,33,1,6,4,88,44] （要求：直接在原列表上处理，不要将结果保存到新列表中）
# list7 = [11,22,33,1,6,4,88,44]
# for i in range(len(list7)-1,-1,-1):
#     if list7[i] < 33:
#         list7.pop(i)
# print(list7)
# 8. 用户输入某年某月某日，利用列表判断这一天是这一年的第几天？
#    思路: 以2021年3月5日为例,需要考虑
#    1).2021年是否为闰年,如果为闰年,那么2月是29天,比平年多1天
# year = 2021
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     list8 = [31,29,31,30,31,30,31,31,30,31,30,31] #闰年的月份列表
# else:
#     list8 = [31,28,31,30,31,30,31,31,30,31,30,31] #平年的月份列表
#
# #    2).3月,那么需要把3月前的满月天数加上,1月天数+2月天数
# month = 3
# month_num = 0
# for i in range(month-1):
#     month_num = month_num + list8[i] #1月天数+2月天数
# # print(month_num)
# #    3).5日,那么需要在日期基础上加上5
# day_num = 5
# zonghe_num = month_num + day_num
# #    4).用列表来记录每月的天数,比较好遍历
# print(f"{year}年{month}月{day_num}日,是这一年的第{zonghe_num}天")

# 9. 用户任意输入一个字符串，输出第 m 个只出现过 n 次的字符
#    比如：在字符串 gbgkkdehh 中，找出第 2 个只出现 1 次的字符，输出结果：d
# list9 = "gbgkkdehh"
# n = 5 #出现次数，可修改
# m = 2 #第几个，可修改
# result = []
# for num in list9:
#     # 判断该数字在列表中出现了 n 次，且尚未加入结果列表
#     if list9.count(num) == n and num not in result:
#         result.append(num)
# if len(result) >= m:
#     print(result[m-1])
# else:
#     print(f"不存在第 {m} 个出现过 {n} 次的字符")
# 不要了：print(result[m-1])  #打印m个出现过n次的字符,索引值得是m-1才行(没有引入判断，如果m超出范围会报错)
# 方法一：列表表达式
# # # 1. 用户输入与参数设置
# text = input("请输入字符串：")  # 例如输入 gbgkkdehh
# n = 1  # 目标出现次数
# m = -1  # 目标第几个
#
# # 2. 用列表推导式过滤出符合条件的字符（按照首次出现顺序且去重）
# targets = [char for char in dict.fromkeys(text) if text.count(char) == n]
#
# # 3. 输出结果判断
# if len(targets) >= m >=1:
#     print(f"第 {m} 个只出现过 {n} 次的字符是：{targets[m-1]}")
# else:
#     print(f"不存在第 {m} 个出现过 {n} 次的字符")
#
# 方法二：使用for
# text = input("请输入字符串：")  # 例如输入 gbgkkdehh
# n = 1   # 目标出现次数
# m = 1  # 目标第几个，从 1 开始
# targets = []
# for char in text:
#     # 判断这个字符是否恰好出现 n 次
#     if text.count(char) == n:
#         # 判断是否已经添加过，避免重复
#         if char not in targets:
#             targets.append(char)
#
# if m < 1:
#     print("m 必须大于等于 1")
# elif m <= len(targets):
#     print(f"第 {m} 个只出现过 {n} 次的字符是：{targets[m - 1]}")
# else:
#     print(f"不存在第 {m} 个出现过 {n} 次的字符")
# 方法三：通过index判断是否第一次加入
# result = []
#
# for i in range(len(numbers)):
#     num = numbers[i]
#
#     if numbers.count(num) == 2 and numbers.index(num) == i:
#         result.append(num)
#
# print(result)
#
# 方法四：使用while
# result = []
# i = 0
#
# while i < len(numbers):
#     num = numbers[i]
#
#     if numbers.count(num) == 2 and num not in result:
#         result.append(num)
#
#     i += 1
#
# print(result)  # [1, 2, 3, 4]
# 方法五：使用字典累计次数
# counts = {}
#
# for num in numbers:
#     if num in counts:
#         counts[num] += 1
#     else:
#         counts[num] = 1
#
# result = []
#
# for num in numbers:
#     if counts[num] == 2 and num not in result:
#         result.append(num)
#
# print(result)

# 方法六：
# text = "gbgkkdehh"
# n = 1  # 目标出现次数
# m = 2  # 目标第几个
#
# # 将字符串转换成列表
# chars = list(text)
#
# # 遍历副本，删除原列表中不符合条件的字符
# for char in chars[:]:
#     if text.count(char) != n:
#         chars.remove(char)
#
# # 去重，并保持第一次出现的顺序
# result = []
#
# for char in chars:
#     if char not in result:
#         result.append(char)
#
# # 判断并输出
# if 1 <= m <= len(result):
#     print(result[m - 1])
# else:
#     print(f"不存在第 {m} 个出现过 {n} 次的字符")

