# 代码题：
# 文件题：
# 要求：定义函数将文件的读写操作封装起来，在每道题目中调用即可，使用with open（），不能使用open()
#
# 定义函数，实现以只读方式打开文件并按read()读取文件
from os import write


def read_file(file):
    with open(file,mode='r',encoding='utf-8') as f:
        res1 = f.read()
    return res1


# 1. 一份文件中保存的是各位同学的各科成绩，编写程序计算出各位同学的总成绩写入文件中每行末尾
# 保存学生成绩的文件格式：
# a1 70 80 90
# a2 80 85 95
# a3 75 60 80
# 注： 以上内容必须以代码的形式写入，不能自行创建一个文件手动写入
#
#定义一个从文件写入的函数
def write_file(file,something):
    with open(file, mode="w", encoding="utf-8") as f:
        f.write(something)
#定义一个从文件追加写入的函数
def awrite_file(file,something):
    with open(file, mode="a", encoding="utf-8") as f:
        f.write(something)

# if __name__ == '__main__':
#     con = write_file('123.txt','a1 70 80 90\na2 80 85 95\na3 75 60 80')
#     print(con)
#     con1 = read_file("123.txt")
#     print(con1)

#定义函数，实现以writelines()给文件写入内容
def writelines_file(file,list1):
    with open(file,mode='w',encoding='utf-8') as f:
        f.writelines(list1)

# 2：构造一个文本文件，文件中有100行数据，数据内容格式为：
#      name   ,  mailbox
#      vu1 , vu1@163.com
#      vu2,vu2@163.com
#      vu3,vu3@163.com
#      ……
#      ……
#
# list1 = []
# for i in range(1,101):
#     c = f"vu{i},vu{i}@163.com\n"
#     list1.append(c)
# if __name__ == '__main__':
#     writelines_file('223.txt', list1)

# 3. 创建文件 fruits.txt 在文件中至少存储三个水果名称,且接受用户的继续输入,当用户结束输入后, 编写一个程序，尝试读取这些文件，统计其字符个数, 并将其内容和总字符数打印到屏幕上。
#
# if __name__ == '__main__':
#     con = write_file("fruits.txt","苹果 西瓜 圣女果 ")
#     con1 = input("请继续输入水果")
#     awrite_file("fruits.txt",con1)
#     con2 = read_file("fruits.txt")
#     # print(f2.tell())
#     nums = len(con2) - con2.count(' ') - con2.count('\n')
#     print(f"内容为：{con2}\n总字符数为{nums}")

# 4. 有名为 username.txt 的文件，其内容格式如下，写一个程序，判断该文件中是否存在'alex'，如果没有，则将字符串'alex'添加到该文件末尾，否则提示用户'该用户已存在'
#       pizza
#       alex
#       egon
def readlines_file(file):
    with open(file,mode='r+',encoding='utf-8') as f:
        res1 = f.readlines()
    return res1
# if __name__ == '__main__':
    # 文件对象名.readlines(): 按行读取文件所有内容
    # # 返回的数据类型是列表，且列表中的每个元素都是str
    # writelines_file("username.txt",["pizza\n","alex\n","egon\n"])
    # a = readlines_file("username.txt")
    # print(a)
    # for i in range(len(a)):
    #     if 'alex' in a[i]:
    #         print("该用户已存在")
    #         break
    # else:
    #     awrite_file("username.txt", "alex")
    # a = read_file("username.txt")
    # print(a)
    #


# 5. 将下列孤勇者的歌词,写代码实现以下要求：
#    1）把每行歌词写入文件中
#    2）统计每行的歌词字数（只统计看得见的），并将字数追加到每行歌词的最后，用空格与歌词隔开
#   歌词内容如下：
#   孤勇者
#   都是勇敢的
#   你额头的伤口 你的不同 你犯的错
#   都不必隐藏
#   你破旧的玩偶 你的面具 你的自我
#   他们说 要带着光 驯服每一头怪兽
#   他们说 要缝好你的伤 没有人爱小丑
#   为何孤独 不可光荣
#   人只有不完美 值得歌颂

# if __name__ == '__main__':
#     list5 = ["孤勇者\n","都是勇敢的\n","你额头的伤口 你的不同 你犯的错\n","都不必隐藏\n","你破旧的玩偶 你的面具 你的自我\n","他们说 要带着光 驯服每一头怪兽\n","他们说 要缝好你的伤 没有人爱小丑\n","为何孤独 不可光荣\n","人只有不完美 值得歌颂\n"]
#
#     # 1. 先把歌词写入文件
#     writelines_file("guyongzhe.txt", list5)
#     # 2. 再把歌词读取出来
#     a = readlines_file("guyongzhe.txt")
#     list6 = []
#     # 3. 统计每行字数
#     for i in range(len(a)):
#         # 总字符数 - 空格 - 换行符
#         b = len(a[i]) - a[i].count(' ') - a[i].count('\n')
#         # 去掉原来的换行符，然后在后面加上字数
#         new_line = a[i].strip('\n') + ' ' + str(b) + '\n'
#         list6.append(new_line)
#     # 4. 把处理后的内容重新写入文件
#     writelines_file("guyongzhe.txt", list6)


# 6. 有名为 user_info.txt的文件，其内容格式如下：
#       pizza,100001
#       alex,100002
#       egon,100003
#       写一个程序实现：
#       1）将id为100002的用户修改为 alex_new
#       2）删除id为100003的行
#
if __name__ == '__main__':
    write_file("user_info.txt","pizza,100001\nalex,100002\negon,100003")
    a = readlines_file("user_info.txt")
    new_list = []
    for line in a:
        # 去掉换行符
        line = line.strip('\n')
        # 按逗号拆分
        user_info = line.split(',')
        name = user_info[0]
        user_id = user_info[1]
        # id为100002，修改用户名
        if user_id == '100002':
            name = 'alex_new'
        # id为100003，直接不添加进新列表，相当于删除
        if user_id == '100003':
            continue
        new_line = name + ',' + user_id + '\n'
        new_list.append(new_line)
    writelines_file("user_info.txt", new_list)