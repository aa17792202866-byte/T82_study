'''
input():   输入函数
作用： 获取用户从键盘输入的数据
input()函数的括号中是可以不写任何内容的，但是为了代码的友好性，一般需要写提示信息
input()函数无论从键盘输入任何数据，返回的数据类型永远都是 str
'''
#定义4个变量，分别保存用户从键盘输入的姓名、性别、年龄、身高；打印每个变量的值及变量的数据类型
#定义变量
name = input('请输入你的姓名:')
sex = input('请输入你的性别:')
age = input('请输入你的年龄:')
height = input('请输入你的身高(单位：cm):')
#打印
print(f'name的值是{name}，数据类型是{type(name)}\nsex的值是{sex}，数据类型是{type(sex)}\nage的值是{age}，数据类型是{type(age)}\nheight的值是{height}，数据类型是{type(height)}')



