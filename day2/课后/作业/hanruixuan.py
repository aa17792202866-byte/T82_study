# 理论题：
# 6.
# python中数据类型转换有哪些函数？数据类型转换要注意什么？
"""
 使用数据类型的同名函数进行转换
 int()、float()、str()、bool()、list()、tuple()、dict()、set()
1. 值的合法性与 ValueError
转换函数要求字符串的内容必须符合目标类型的语法。
2. 精度丢失问题
浮点数转整数： int(float_val) 不会进行四舍五入，而是直接向下截断（抛弃小数部分）。
例如：int(3.99)  # 结果为 3
如果需要四舍五入，应使用 round() 函数（注意 Python 的 round() 是银行家舍入法，如果恰好是5，看前面是否是奇数，奇数的话进一位数，偶数直接舍去）。
大浮点数精度： 浮点数存在二进制表示精度局限，转换或计算时可能出现 0.1 + 0.2 != 0.3 的情况，精度敏感场景（如金融）应使用 decimal.Decimal。
3. 布尔值（Truthy / Falsy）转换规则
使用 bool() 转换时，只有以下“空值/零值”会被转为 False，其余全为 True：
数字 0、0.0、0j
空容器：""（空字符串）、[]（空列表）、()（空元组）、{}（空字典）、set()
特殊值：None 和 False
坑点： 字符串 "False" 或 "0" 转换后均为 True（因为它们是非空字符串）。
4. 容器转换是的“非原位”特性与去重（还没讲）  注：“非原位” 是指转换操作不会在原本的数据内存空间里直接修改数据，而是会创建一个全新的对象/容器。
去重与无序： 将列表转为 set 可以快速去重，但会丢失原本的元素顺序（若需保持顺序可用 dict.fromkeys()）。
字典转换要求： dict() 转换的参数必须是双值子序列（如元组列表 [(k1, v1), (k2, v2)]）或使用关键字参数。
5. 隐式类型转换（Implicit Conversion）
Python 在进行混合类型运算时，会自动将较低精度的类型提升为较高精度的类型，以防止数据丢失：
例如：
a = 10     # int
b = 2.5    # float
c = a + b  # c 自动变为 float (12.5)
"""


# 7.
# 判断结构有哪几种？通过什么判断要执行分支中的哪个执行语句？
'''
已讲三种：
1. 单if结构
2. if-else结构
3. if-elif-elif-else结构
4.在 match-case 结构中：取决于“模式匹配（Pattern Matching）”（未讲）
判断依据： 将 match 关键字后面的变量/表达式，与各个 case 预设的模式或值进行比对。

1. 在 if / elif / else 结构中：取决于“布尔值（True / False）”
判断依据： if 或 elif 关键字后面紧跟的条件表达式（Condition Expression）。

计算过程： Python 会对条件表达式进行求值，并将其隐式转换为布尔值：

如果求值结果为 True（或非零数字、非空容器等“真值”），则执行该分支下的代码块，并直接跳过后续的所有 elif 和 else。

如果求值结果为 False（或 0、None、空容器等“假值”），则跳过当前分支，继续向上向下依次判断下一个 elif 的条件。

如果所有条件表达式计算结果均为 False，且存在 else 块，则执行 else 内部的语句。

2. 在 match-case 结构中：取决于“模式匹配（Pattern Matching）”
判断依据： 将 match 关键字后面的变量/表达式，与各个 case 预设的模式或值进行比对。

计算过程： 从上到下依次匹配，第一个与目标值类型/结构/数值成功匹配的 case 分支会被执行。

'''


# 8.
# 判断语句中, 构成条件语句的所有运算符或特殊数值?
'''
1. 比较运算符
   ==	 检查==左右两边的值是否相等，如果是则条件变为真。
   is    检查is左右两端是否同一个对象(即：内存给其分配的空间地址值是否一致)，如果是则条件变为真。
   !=	 检查!=左右两边的值是否相等，如果值不相等，则条件变为真。
   >	 检查>左边的值是否大于右边的值，如果是，则条件成立。
   <	 检查<左边的值是否小于右边的值，如果是，则条件成立。
   >=	 检查>=左边的值是否大于或等于右边的值，如果是，则条件成立。
   <=	 检查<=左边的值是否小于或等于右边的值，如果是，则条件成立。
2. 逻辑运算符
   and    且，与  所有条件均满足
   or     或，满足任意一个即可
   not    非，取反
3. 记住一些特殊值
   除了数字0、空字符串、空列表、空元组、空字典、空值None转为False，其他皆为True
'''
#
#
# 代码题：
# 判断语句题目：
# 1. 编写程序，从键盘获取用户名和密码，然后判断(自己预先设定一个正确的用户名和密码)，如果正确就输出以下信息
#     =============================================
#     =       亲爱的XXX,欢迎进入到身份认证系统V1.0
#     = 1. 登录
#     = 2. 退出
#     = 3. 认证
#     = 4. 修改密码
#     =============================================
# 如果不正确,就提示用户”Bye bye!”


# user_name1='韩瑞轩'
# user_password1= 2003
# user_name2=input("请输入用户名")
# user_password2=int(input("请输入密码"))
# if user_name1 == user_name2 and user_password1 == user_password2:
#     print('=============================================')
#     print('=       亲爱的XXX,欢迎进入到身份认证系统V1.0')
#     print('= 1. 登录\n= 2. 退出\n= 3. 认证\n= 4. 修改密码')
#     print('=============================================')
# else:
#     print('Bye bye!')

# 2.企业发放的奖金根据利润提成,利润低于或等于10万元时,奖金可提成10%,利润高于10万元时,低于20万元时,低于10万元部分按10%提成,高于10万元部分按7.5%提成,20-40万时,高于20万部分,可提成5%,40-60万时,高于40万部分,可提成3%,60-100万时,高于60万部分,可提成1.5%,高于100万的部分,可提成1%,从键盘输入当月利润,求应发放的奖金总数?
Profit = float(input('请输入当月利润'))
if Profit<0:
    print('利润不能为负数')
elif Profit<=100000:
    print(f"应该发放的奖金数总数为{Profit*0.1}")
elif Profit<=200000:
    print(f"应该发放的奖金数总数为{100000 * 0.1 + (Profit-100000) * 0.075}")
elif Profit<=400000:
    print(f"应该发放的奖金数总数为{100000 * 0.1 + 100000 * 0.075 + (Profit-200000) * 0.05 }")
elif Profit<=600000:
    print(f"应该发放的奖金数总数为{100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (Profit-400000) * 0.03 }")
elif Profit<=1000000:
    print(f"应该发放的奖金数总数为{100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (Profit-600000) * 0.015}")
else:
    print(f"应该发放的奖金数总数为{100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 +(Profit-1000000) * 0.01}")
# 3.输入用户的身高信息,单位为米，输入用户的体重信息,单位为kg。请根据BMI公式（体重除以身高的平方）帮用户计算他的BMI指数，并根据BMI指数给出对应的提示信息：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
height = float(input("请输入您的身高(单位：m)"))
weight = float(input("请输入您的体重(单位：kg)"))
bmi = weight / (height**2)
print(1.0+2.0)
print(weight)
print(height)

print(bmi)
if not 0<=height<=2.5 and weight > 0:
    print("您的输入超出系统范围")
elif bmi < 18.5:
    print("过轻")
elif bmi < 25:
    print("正常")
elif bmi < 28:
    print("过重")
elif bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")


# 4.请根据男女,输入你的各项参数,计算你的体脂率:
# 成年女性的体脂率计算公式：
# 参数a=腰围（cm）×0.74
# 参数b=体重（kg）×0.082+34.89
# 体脂肪重量（kg）=a－b
# 体脂率=（身体脂肪总重量÷体重）×100%
# 成年男性的体脂率计算公式：
# 参数a=腰围（cm）×0.74
# 参数b=体重（kg）×0.082+44.74
# 体脂肪重量（kg）=a－b
# 体脂率=（身体脂肪总重量÷体重）×100%。
# 成年人的体脂率正常范围分别是女性20%～25%，男性15%～18%，若体脂率过高，就有肥胖的风险。请提示用户是否可能属于肥胖。
gender = input("请输入您的性别:")
if gender == '女':
    waist_cm = float(input("请输入您的腰围(单位：cm)："))
    weight_kg = float(input("请输入您的体重(单位：kg)"))
    a = waist_cm * 0.74
    b = weight_kg*0.082+34.89
    tizhifang = a-b
    tizhilv = (a-b)/weight_kg *100
    if tizhilv<=0:
        print("您的体脂率小于或等于0，请重新输入")
    elif tizhilv <= 25:
        print(f"您的体脂率是{tizhilv}%")
    else:
        print(f"您的体脂率是{tizhilv}%,可能属于肥胖")
elif gender == '男':
    waist_cm = float(input("请输入您的腰围(单位：cm)："))
    weight_kg = float(input("请输入您的体重(单位：kg)"))
    a = waist_cm * 0.74
    b = weight_kg*0.082+44.74
    tizhifang = a-b
    tizhilv = (a-b)/weight_kg * 100
    if tizhilv<=0:
        print("您的体脂率小于或等于0，请重新输入")
    elif tizhilv <= 18:
        print(f"您的体脂率是{tizhilv}%")
    else:
        print(f"您的体脂率是{tizhilv}%,可能属于肥胖")
else:
    print('请输入正确性别')

# 5.用户和计算机玩石头剪刀布的游戏，计算机随机出一个(其中：0代表石头，1代表剪刀，2代表布)，由人来猜；
#    如果人猜的与计算机出的一致，则打印“平局”
#    如果人赢了，则打印“你赢了”，否则打印“你输了”

# import random
# #定义变量，保存计算机随机出的一个100以内的正整数
# com_shuchu = random.randint(0,2)
# # print(f"{com_shuchu}")
# user_shuru = int(input("请输入数字出拳(其中：0代表石头，1代表剪刀，2代表布)"))
# if user_shuru == 0 or user_shuru == 1 or user_shuru == 2: #判断是否为0，1，2
#
#     if com_shuchu == user_shuru: #判断是否平局
#         print('平局')
#     elif (user_shuru == 0 and com_shuchu == 1) or (user_shuru == 1 and com_shuchu == 2) or (user_shuru == 2 and com_shuchu == 0):
#         print('你赢了')
#     else:
#         print('你输了')
# else:
#     print('请输入0、1、2中的一个数字')










# if com_shuchu == 0 or com_shuchu == 1 or com_shuchu == 2 and com_shuchu == user_shuru:
#     print('平局')
#     if com_shuchu == 0 and user_shuru == 2:
#         print('你赢了')
#     else:
#         print('你输了')
#     if com_shuchu == 1 and user_shuru == 0:
#         print('你赢了')
#     else:
#         print('你输了')
#     if com_shuchu == 2 and user_shuru == 1:
#         print('你赢了')
#     else:
#         print('你输了')
# else:
#     print('请输入0、1、2中的一个数字')