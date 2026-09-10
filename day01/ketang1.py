#定义5个变量，分别用来保存姓名、性别、年龄、身高，住址；打印“XXX是一名家住XXX，身高为XXXcm的XXX岁的XXX性”
# 其中： 身高保留1位小数
# 要求：分别使用普通输出和两种格式化输出的方式打印

name = '韩瑞轩'
sex = '男'
age = 23
height = 180.00
address = '西安市雁塔区三迪枫丹'
print(f'{name}是一名家住{address},身高为{round(height)}cm的{age}岁的{sex}性')
print(f'{name}是一名家住{address},身高为{height:.2f}cm的{age}岁的{sex}性')
print('%s是一名家住%s,身高为%.2fcm的%d岁的%s性'%(name,address,height,age,sex))
print("韩瑞轩是一名家住西安市雁塔区三迪枫丹，身高为180.0cm的23岁的男性")
