# 编写函数：接收输入一个字符，判断这个字符是数字，还是大写字母，还是小写字母，还是符号(ASCII码)
def is_ascii(a1):
    if a1.isascii():
        return True

def is_one(str1):
    if len(str1) == 1:
        return True

def is_num(str1):
    if str1.isdigit():
        return True

if __name__ == '__main__':

    user = input("请输入字符")
    if is_one(user): #判断字符串是不是一个字符

        if is_ascii(user):
            print(f"{user}是一个ASCII字符")
            if is_num(user):
                print(f"{user}是一个数字")

    else:
        print(f"{user}不是一个ASCII字符")