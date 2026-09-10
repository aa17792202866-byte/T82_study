'''
数据类型转换：
使用数据类型的同名函数进行转换
int()、float()、str()、bool()、list()、tuple()、dict()、set()

1. 其他数据类型转整数型： int()
   str-->int:         只有字符串的内容为整数时，才可转
   float-->int:       可转，只取整数位,精度损失
   bool-->int:        可转，True转为1，False转为0
    

2. 其他数据类型转浮点型： float()
   str-->float：      只有字符串的内容为数字时，才可转
   int-->float:       可转，转为: 整数.0
   bool-->float:      可转，True转为1.0，False转为0.0

3. 其他数据类型转字符串： str()
   一切皆可转

4. 其他数据类型转布尔型： bool()
   除了数字0、空字符串、空列表、空元组、空字典、空值None转为False，其他皆为True

'''
# # 问题:假如我们现在编写一个记账软件,通过用户手动输入每天的收入和支付情况,程序可以给出当天的一个收益盈亏的情况,那么这个代码该怎么实现?
# #定义2个变量，分别保存用户从键盘输入的收入和支出金额
# shouru = int(input('请输入当日的收入金额(单位：元)'))
# zhichu = int(input('请输入当日的支出金额(单位：元)'))
# #计算盈亏
# yk = shouru - zhichu
# # yk = int(shouru) - int(zhichu)
# #打印结果
# print(f'您当日收入{shouru}元，支出{zhichu}元，盈亏是{yk}元')

# # str-->int:
# print(int('1'),type(int('1')))        #1  int
# print(int('-1'),type(int('-1')))      #-1  int
# print(int('0'),type(int('0')))        #0  int
# print(int('1.1'),type(int('1.1')))      #报错
# print(int('a'),type(int('a')))        #报错
# print(int('+'),type(int('+')))      #报错
# print(int('我'),type(int('我')))      #报错

# # float-->int:
# print(int(1.1),type(int(1.1)))     #1  int
# print(int(1.9),type(int(1.9)))     #1  int
# print(int(-1.99999),type(int(-1.99999)))     #-1  int

# # bool-->int:
# print(int(True),type(int(True)))      #1  int
# print(int(False),type(int(False)))      #0  int

# # str-->float：
# print(float('1'),type(float('1')))     #1.0   float
# print(float('-1'),type(float('-1')))     #-1.0   float
# print(float('0'),type(float('0')))     #0.0   float
# print(float('-1.99'),type(float('-1.99')))     #-1.99   float
# # print(float('a'),type(float('a')))     #报错
# # print(float('我'),type(float('我')))     #报错

# # int-->float:
# print(float(1),type(float(1)))       #1.0  float
# print(float(-1),type(float(-1)))       #-1.0  float
# print(float(0),type(float(0)))       #1.0  float

# # bool-->float:
# print(float(True),type(float(True)))    #1.0  float
# print(float(False),type(float(False)))    #1.0  float

# #int-->str:
# print(str(1),type(str(1)))      #'1'  str
# print(str(0),type(str(0)))      #'0'  str
# print(str(-1),type(str(-1)))      #'-1'  str
#
# # float-->str:
# print(str(1.99),type(str(1.99)))      #'1.99'  str
#
# # bool-->str:
# print(str(True),type(str(True)))      #'True'  str
#
# print(str([11,22]),type(str([11,22])))      #'[11,22]'  str
# print(str((11,22)),type(str((11,22))))      #'(11, 22)'  str
# print(str({'name':'张三'}),type(str({'name':'张三'})))
# print(str({1,2,3}),type(str({1,2,3})))

# int-->bool:
print(bool(1),type(bool(1)))     #True  bool
print(bool(0),type(bool(0)))     #False  bool
print(bool(-1),type(bool(-1)))     #True  bool
print(bool(1001),type(bool(1001)))     #True  bool
print(bool(-1001),type(bool(-1001)))     #True  bool

# float-->bool:
print(bool(1.0),type(bool(1.0)))     #True  bool
print(bool(0.0),type(bool(0.0)))     #False  bool
print(bool(0.9),type(bool(0.9)))     #True  bool

# str-->bool:
print(bool('1'),type(bool('1')))     #True  bool
print(bool('0'),type(bool('0')))     #True  bool
print(bool('a'),type(bool('a')))     #True  bool
print(bool('刘毅'),type(bool('刘毅')))     #True  bool
print(bool(' '),type(bool(' ')))     #True  bool
print(bool(''),type(bool('')))     #False  bool

# list--bool:
print(bool([1,2]),type(bool([1,2])))   #True  bool
print(bool([]),type(bool([])))   #False  bool

# tuple--bool:
print(bool((1,2)),type(bool((1,2))))   #True  bool
print(bool(( )),type(bool(( ))))   #False  bool

# dict-->bool:
print(bool({1:1}),type(bool({1:1})))
print(bool({}),type(bool({})))

#None-->int:
print(type(None))
print(bool(None),type(bool(None)))

# # ord():  返回一个字符对应ASCII码表中的十进制整数
# print(ord('a'))       #97
# print(ord('z'))       #122
# print(ord('Z'))       #90
# print(ord('A'))       #65

