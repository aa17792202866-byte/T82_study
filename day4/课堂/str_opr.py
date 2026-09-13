'''
字符串： str
作用： 用来在程序中显示消息,保存数据,传输数据.

1. 表示方式
   以单引号、双引号、三引号作为标识

2. 输入
   input()

3. 输出
   print()

4. 索引下标
   索引，就相当于内存给字符串中的每个字符编了个独一无二的号
   因为字符串在内存中是连续存储的，内存给字符串的首字符默认编号为0，以此类推
   通过索引值查找对应的字符：   字符串[索引值]        注：索引值必须存在

5. 切片
   切片是指对字符串截取其中一部分的操作
   切片的语法： [start:end:step]
   切片中的几个参数说明：
    1） start：     开始值(索引值)    可以不写，默认为0；如果写了则以实际为准
    2） end：       结束值(索引值)    可以不写，默认取到最后一个字符；
                                      如果写了，则取到end的前一个
    3） step：      步长/步距         可以不写，默认为1；如果写了则以实际为准

    记住一些特殊的
    [:]         取全部
    [::-1]      逆序/翻转
    [:n]        取前n个字符
    [n:]        除了前n个不取，剩下的全取
    [-n:]       取后n个字符
    [:-n]       除了后n个不取，剩下的全取

6. 字符串的遍历
   1）方式一： 只知道具体的字符，但不知道其索引值
    语法格式：
    for 临时变量 in 字符串:
        print(临时变量)

    2）方式二： 不仅知道具体的字符，还知道其对应的索引值
    语法格式：
    for 临时变量 in range(len(字符串)):
        print(临时变量,字符串[临时变量])

7. 常见操作(函数)
1）len(字符串)：      返回字符串的字符总个数(长度)
2）目标字符串.find(指定字符串):
   从左往右检索目标字符串中是否存在指定的字符串，如果存在则返回指定字符串从左往右在目标字符串中第一次出现的首字符对应的索引值；否则返回-1
3）目标字符串.rfind(指定字符串):
   从右往左检索目标字符串中是否存在指定的字符串，如果存在则返回指定字符串从右往左在目标字符串中第一次出现的首字符对应的索引值；否则返回-1
4）目标字符串.split(sep,maxsplit):  主要用于实现将 字符串 转 列表
   主要参数说明：
    sep:        切割符       可以不写，默认为一个空格；如果写了则以实际为准
    maxsplit    最大切割数   可以不写，以实际为准
                             如果写了且大于等于实际可切割数，则以实际为准
                             如果写了且小于实际可切割数，则从左往右按照设置的最大切割数进行切割
                             ，剩下的归为一个子串
5）拼接符.join(列表):     主要用于实现将 列表  转  字符串
6）目标字符串.isdigit():  判断目标字符串是纯数字，则返回True;否则返回False
7）目标字符串.isalpha():  判断目标字符串是纯字母，则返回True;否则返回False
8）目标字符串.isalnum():  判断目标字符串是纯数字/纯字母/字母+数字，则返回True;否则返回False
9）目标字符串.count(指定字符串)：   统计指定字符串在目标字符串出现的次数
10）目标字符串.replace(old,new,count):  替换
     old：    替换前的原字符串内容      必须要写
     new:     替换后的新内容            必须要写
     count:    替换几处                 可以不写，以实际为准
11）目标字符串.upper():    将目标字符串转大写
12）目标字符串.lower():    将目标字符串转小写
13）目标字符串.isupper():    判断目标字符串是大写，则返回True；否则返回False
14）目标字符串.islower():    判断目标字符串是小写，则返回True；否则返回False
15）目标字符串.startswith():  判断目标字符串是否以指定的字符串开头，是则返回True,否则返回False
16）目标字符串.endswith():    判断目标字符串是否以指定的字符串结尾，是则返回True,否则返回False


'''
# name = 'abcdefeg'
# print(name[4])      #'e'
# print(name[6])      #'e'
# # print(name[10])     #报错
# print(name[-1])     #'g'
# print(name[-4])     #'e'
# # print(name[-10])    #报错

# name = '12345abcde你我他$%&'
# print(name[4])        #通过索引值查找对应的字符
# print(name[2:7:1],type(name[2:7:1]))    #345ab   str
# print(name[4:8:2])    #5b
# print(name[3:9:-3])   #''
# print(name[9:3:-3])   #eb
# print(name[-3:-9:-3]) #$你
# print(name[4:7])      #5ab
# print(name[7:2])      #''
# print(name[:3])       #123    取前3个字符
# print(name[3:])       #45abcde你我他$%&   除了前3个字符不取，剩下的全取
# print(name[:-3])      #12345abcde你我他   除了后3个字符不取，剩下的全取
# print(name[-3:])      #$%&  只取后3个字符
# print(name[:])        #12345abcde你我他$%&      取全部
# print(name[::-1])     #&%$他我你edcba54321      逆序/翻转

# name = '12345abcde你我他$%&'
# # 1）打印name中的每一个字符，打印成一行
# for i in name:
#     print(i,end=' ')
# # 2）打印name中的每个字符及其对应的索引值
# for i in range(len(name)):   #i:[0,1,2,3,4....15]
#     print(i,name[i])

# str1 = 'xabc123abcedfabdyz'
# # 1)查找str1中是否存在‘z’
# print(str1.find('z'))      #17
# # 2)查找str1中是否存在‘y’
# print(str1.find('y'))      #16
# # 3)查找str1中是否存在‘x’
# print(str1.find('x'))       #0
# # 4)查找str1中是否存在‘yz’
# print(str1.find('yz'))      #16
# # 5)查找str1中是否存在‘a’
# print(str1.find('a'))      #1
# # 6)查找str1中是否存在‘bc’
# print(str1.find('bce'))      #8
# # 7)查找str1中是否存在‘bcbc’
# print(str1.find('bcbc'))      #-1


# # 1.从请求地址中提取出用户名和域名http://www.163.com?userName=admin&pwd=123456
# url = 'http://www.163.com?userName=admin&pwd=123456'
# print(url[7:18],url[28:33],url[-16:-11])
# print(url[url.find('w'):url.find('?')],url[url.find('=')+1:url.find('&')])
#
# # # 2.根据完整路径从路径中分离文件路径，文件名及文件扩展名
# # # 注意python中一个反斜杠有特殊含义，所以要用二个反斜杠
# # # str2 = "D:\\软件\python\\python39\\Tools\scripts\\abitype.py"
# str2 = "D:\\软件\python\\python39\\Tools\scripts\\abitype.py"
# print(str2[:35],str2[:-11],str2[:str2.rfind('\\')])
# print(str2[36:43],str2[-10:-3],str2[str2.rfind('\\')+1:-3])
# print(str2[-3:])

# str4 = '嗯嗯 晚安 好梦 想你 明天见'
# print(str4)
# # 1）将str4以一个空格为切割符，进行切割
# print(str4.split(' '))
# print(str4.split())
# print(str4.split('好梦'))
# # 2）将str4以一空格作为切割符，切5下
# print(str4.split(' ',5))
# print(str4.split(' ',4))
# print(str4.split(' ',2))
#
# list2 = ['嗯嗯', '晚安', '好梦', '想你', '明天见']
# # 1)将list2中的元素无缝拼接成一个字符串
# print(''.join(list2))
# # 1)将list2中的元素拼接成一个空格
# print(' '.join(list2),type(' '.join(list2)))

# str5 = '123456'
# str6 = 'abcdBDDD'
# str7 = '123abcABC'
# str8 = '1111abc我'
# print(str5.isdigit())       #True
# print(str6.isalpha())       #True
# print(str7.isalnum())       #True
# print(str5.isalnum())       #True
# print(str6.isalnum())       #True
# print(str8.isdigit())       #False
# #打印并统计str8中共计多少个数字？
# nums = 0
# for i in str8:
#     if i.isdigit():
#         nums += 1
# print(nums)

# str9 = 'abcdabcabcabca'
# # 1)统计str9中共计几个'a'
# #定义变量
# nums = 0
# #遍历str9：
# for i in str9:
#     if i == 'a':
#         nums += 1
# print(nums)
# print(str9.count('a'))     #4
# # 2)统计str9中共计几个'abc'
# print(str9.count('abc'))     #4


# str10 = 'good good study,day day up'
# print(str10.replace('good','好').replace('study','学习').replace('day','天').replace('up','向上'))

str6 = 'abcABC我$%111'
print(str6.upper())
print(str6.lower())
print(str6.startswith('abc'))   #True
print(str6.endswith('111'))   #True






