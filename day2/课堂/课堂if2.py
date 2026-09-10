


num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))
res1 = num1 + num2
res2 = num1 - num2

if num1 < num2:
    print(f"第一个数字小于第二个数字，进行加法运算：{num1}+{num2}={res1}")
else:
    print(f"第一个数字大于等于第二个数字，进行减法运算：{num1}-{num2}={res2}")