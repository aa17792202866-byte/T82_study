# 1. 常量和变量的区分？
# 常量：具备字面的含义，可以按照字面上的含义使用它们的值，这就是常量。常量的值不能改变。
# 变量：一般我们把经常变化的值用变量来存储和表示,代码中调用和修改变量,并不直接去接触和修改真正的数值。
# 2. 写出变量命名时的规则？
# ①变量名只能包含字母、数字和下划线。变量名可以以字母或下划线打头，但不能以数字打头；
# ②变量名不能包含空格，但可使用下划线来分隔其中的单词；
# ③不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词；
# ④变量名应既简短又具有描述性；
# ⑤慎用小写字母l和大写字母O.
# 3.python中简单的数据类型有哪些？字符串怎么表示?
#   数据类型：①int：整数；②float：浮点型（小数）；③str：字符串；④bool：布尔型，只有True和False
#   字符串的表示：使用单引号、双引号、三引号
# 4.python中复杂的数据类型有哪些（数据结构）？
#   复杂的数据类型：①list：列表；②tuple：元组；③dict：字典。
# 5.python中字符串内容怎么做转义?字符串的格式化两种写法？
#   ①\n:换行
#     \'：'
#     \"："
#     \t：横向制表符，横向产生四个空字符，与敲‘Tab’键效果一样
#     \v：纵向制表符，纵向产生四个空字符
#   ②占位符（%）或者f'{变量名}不可变部分'
# 1. 使用print()函数输出“Hello World！HZDL{3}”
#    1)word!后换行输出
print('Hello World!\nHZDL{3}')
#    2)不换行输出
print("Hello World!HZDL{3}")
#    3)把数字3和其它部分用|隔开
print("Hello World!HZDL{",3,"}",sep='|')
# 2. 用两种方式将  It's Sunday today！ 打印输出
print("It's Sunday today！")  #字符串本身有单引号
print('It\'s Sunday today！')  #转义符
# 3. 输出 c:\trasert\net.txt
print(r'c:\trasert\net.txt')  #原始字符串
print('c:\\trasert\\net.txt')  #\\2个反斜杠
# 4. 使用print(“hello\n”*8)和print(“hello”*8)看输出结果
print("hello\n"*8)    #换行输出8个hello
print("hello"*8)      #不换行连续输出8个hello
#  5. 格式化输出个人名片。
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

name='张颖'
company='汇智动力'
position='董事长'
phone=16888888888
email='88888.@qq.com'
pay=1000000000000.88
star='*'*40

# 第一种(普通输出)：
print(star,'\n','公司名称:',company,'\n','姓名(',position,'):',name,'\n','电话:',phone,'\n','邮箱:',email,'\n','工资:',round(pay,2),'\n',star,sep='')

# 第二种（占位符）：
print('%s\n公司名称:%s\n姓名(%s):%s\n电话:%s\n邮箱:%s\n工资:%.2f\n%s'%(star,company,position,name,phone,email,pay,star))

# 第三种（格式化输出）:
print(f'{star}\n公司名称:{company}\n姓名({position}):{name}\n电话:{phone}\n邮箱:{email}\n工资:{pay:.2f}\n{star}')

