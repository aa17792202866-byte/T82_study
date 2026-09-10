# 理论题：
# 1. 常量和变量的区分？
# 常量运行过程中不变，变量运行过程中可以改变
# 2. 写出变量命名时的规则？
# 英文、_、数字组成，数字不能开头，不能使用python关键字做变量名
# 3.python中简单的数据类型有哪些？字符串怎么表示?
# int float bool str
#'' or "" or """ """

# 4.python中复杂的数据类型有哪些（数据结构）？
# 列表（list）、元组（tuple）、字典（dict）
# 5.python中字符串内容怎么做转义?字符串的格式化两种写法？
#字符串转义
# path = "C:\\new\\test"
# path = r"C:\new\test"
# | 转义符 | 含义 |
# | `\n` | 换行 |
# | `\t` | 制表符（Tab） |
# | `\'` | 单引号 |
# | `\"` | 双引号 |
# | `\\` | 反斜杠 |
# 代码题：
# 1. 使用print()函数输出“Hello World！HZDL{3}”
#    1)word!后换行输出
# print("Hello World！\nHZDL{3}")
#    2)不换行输出
# print("Hello World！HZDL{3}")
#    3)把数字3和其它部分用|隔开
# print("Hello World！HZDL{|3|}")

# 2. 用两种方式将  It's Sunday today！ 打印输出
# print("It's Sunday today！")
# print('It\'s Sunday today！')

# 3. 输出 c:\trasert\net.txt
# print(r'c:\trasert\net.txt')

# 4. 使用print(“hello\n”*8)和print(“hello”*8)看输出结果
# print("hello\n"*8)
# print("hello"*8)
# 5. 格式化输出个人名片。
# 定义变量：姓名，公司，职位，电话，邮箱,工资(小数点后保留2位)。按照以下格式输出：
# **************************************************
# 公司名称 :
# 姓名(职位):
# 电话：
# 邮箱：
# 工资:
# **************************************************
# 注意：两行星星也要打印
# 要求使用三种方式分别打印名片
name="张三"
company="随便公司"
position="经理"
telephone="17792202866"
email="17792202866@163.com"
salary= 8000.00
star="**************************************************"

print(star,'\n公司名称：',company,'\n姓名(职位)：',name,'(',position,')','\n电话：',telephone,'\n邮箱：',email,'\n工资：',round(salary,2),'\n',star,sep="")

print("%s\n公司名称：%s\n姓名(职位)：%s(%s)\n电话：%s\n邮箱：%s\n工资：%.2f\n%s"%(star,company,name,position,telephone,email,salary,star))
print(f"{star}\n公司名称: {company}\n姓名(职位): {name}({position})\n电话: {telephone}\n邮箱: {email}\n工资: {salary:.2f}\n{star}")

# 定义4个变量，分别保存用户从键盘输入的姓名、性别、年龄、身高
name = input("请输入姓名：")
gender = input("请输入性别：")
age = int(input("请输入年龄："))
height = float(input("请输入身高："))
