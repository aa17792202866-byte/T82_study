# 1. 定义一个函数，实现两个数字的减法运算的结果
def jianfa(num1,num2):
    return num1 - num2
# 3. 定义一个函数，实现计算一个四位正整数上的每位数字之和
# def meiweishuzihe(num3):
#     sum3 = 0
#     # num3 = str(num3)
#     for i in str(num3):
#         sum3 += int(i)
#     return sum3
#
# if __name__ == '__main__':
#     print(jianfa(2,1))
#     print(meiweishuzihe(1234))

def print_stars():
    for i in range(1, 10):
        print("*" * i)

# 调用函数
print_stars()