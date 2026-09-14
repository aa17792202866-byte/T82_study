'''
列表：  list
列表是一种复杂的数据类型(数据结构)，可以存储多个值及多种数据类型
列表是可变数据类型

1. 表示方式
   以[]作为标识，[元素1，元素2，元素3，...]
   []:  空列表

2. 列表与字符串互转
   字符串转列表：  split()
   列表转字符串：  join()

3. 索引
   同字符串
   通过索引值查找对应的元素：   列表[索引值]

4. 切片
   同字符串

5. 列表的遍历
   1）方式一： 只知道具体的元素，不知道其对应的索引值
   语法格式：
   for 临时变量 in 列表:
        print(临时变量)

   2）方式二： 不仅知道具体的元素，还知道其对应的索引值
   语法格式：
   for 临时变量 in range(len(列表))：
        print(临时变量，列表[临时变量])

7. 增加
   1）列表.append(元素值):         给列表中的最后添加一个新的元素
   2）列表.insert(索引值,元素值):  给指定索引值对应元位置的前面插入一个新的元素
   3）列表.extend(列表):           将extend()括号中的列表里面的所有元素依次追加到目标列表的最后

8. 修改
   语法格式：  列表[索引值] = 新值

9. 删除
   1）列表.pop(索引值):     根据索引值删除对应位置的元素，返回本次删除的元素值
                            没有参数的情况下，默认删除最后一个元素
                            有参数(索引值)的情况下，删除索引对应位置的元素
   2) 列表.remove(元素值):  根据元素值删除对应位置的元素
                            如果被删除的元素值存在多个，则每次只删除从左往右出现的第一个该元素值
   3）del 列表[索引值]:     根据索引值删除对应位置的元素
      del 列表:             删除整个列表
      列表.clear():         清空列表

10. 查询
   1）通过索引值查找对应的元素：       列表[索引值]      注:索引值必须存在，否则报错
   2）列表.index(元素值)：       通过元素值查找对应的索引值      注:元素值必须存在，否则报错
                                 如果要查查找的元素值在目标列表中存在多个，则只返回从左往右第
                                 一次出现该元素值对应的索引值
   3）列表.count(元素值)：       返回指定的元素值在目标列表中出现的次数
   4）元素 in 列表：             如果元素存在于列表中则返回True；否则返回False
      元素 not in 列表:          如果元素不存在于列表中则返回True；否则返回False

11. 排序
   1）列表.sort():
      不写参数时，默认将列表中的所有元素从小到大(升序)排序，且将排序后的结果自动更新到原列表中（本质：修改），不可逆
      如果要将列表进行从大到小(降序)排序，则需要使用： 列表.sort(reverse=True)

   2）sorted(列表):
      不写参数时，默认将列表中的所有元素从小到大(升序)排序，且将排序后的结果保存一个新的列表中，不影响原列表；
      如果要将列表进行从大到小(降序)排序，则需要使用： sorted(列表,reverse=True)

   3）列表.reverse():     逆序/翻转
      列表[::-1]:         逆序/翻转

12. 常见操作
    1）len(列表)：      返回列表的元素总个数(即：长度)
    2）max(列表)：      返回列表中最大的元素
    3）min(列表)：      返回列表中最大的元素
    4）sum(列表):       返回列表中所有元素的和
'''
# list1 = ['张三','男',18,188.89,'陕西',True]
# print(type(list1),list1)
#
# print(list1[2])    #18
# # print(list1[6])    #报错
# print(list1[-2])     #'陕西'
# # print(list1[-8])     #报错

# list2 = ['张三','男',18,188.89,'陕西',True,99,1111,45.55]
# print(list2[2:8:3])        #[18,True]
# print(list2[1:6:2])        #['男',188.89,True]
# print(list2[4:6:-1])       #[]
# print(list2[-6:-4:2])      #[188.89]
# print(list2[3:-4:-1])      # []
# print(list2[3:15:1])       #[188.89, '陕西', True, 99, 1111, 45.55]
# print(list2[-15:-3:1])     # ['张三', '男', 18, 188.89, '陕西', True]
# print(list2[:])            #['张三', '男', 18, 188.89, '陕西', True, 99, 1111, 45.55]
# print(list2[:3])           #['张三', '男', 18]
# print(list2[3:])           #[188.89, '陕西', True, 99, 1111, 45.55]
# print(list2[:-3])          #['张三', '男', 18, 188.89, '陕西', True]
# print(list2[-3:])          #[99, 1111, 45.55]
# print(list2[::-1])         #[45.55, 1111, 99, True, '陕西', 188.89, 18, '男', '张三']

# list3 = ['张三','男',18,188.89,'陕西',True,99,1111,45.55]
# # 1)打印list3中的每一个元素
# for i in list3:
#     print(i,type(i),end=' ')
# # 2)打印list3中的每一个元素及对应的索引值
# for i in range(len(list3)):
#     print(i,list3[i])

# list4 = ['张三','男',18,188.89,'陕西',True,99,1111,45.55]
# print(list4)
# # 1)给list4中新增一个'中国人'
# print(list4.append('中国人'))    #打印append()函数返回的结果   None
# print(list4)
# list4.append('中国人')
# print(list4)
# # 3)给第一个'中国人'的前面插入一个100
# list4.insert(9,100)
# print(list4)
# list4.insert(-2,1001)
# print(list4)
# list4.insert(90,'九十')
# print(list4)
# list4.insert(-90,'负九十')
# print(list4)
# # 3)将[11,22,33]这个列表中的元素插入到list4中
# # for i in [11,22,33]:     #i:  11,22,33
# #     list4.append(i)
# # print(list4)
# list4.extend([11,22,33])
# print(list4)
# # 4）将list4中的第一个‘中国人’修改为‘日本人’
# list4[-6] = '日本人'
# print(list4)
# list4[13] = '日本人'
# print(list4)
# # list4[-60] = '日本人'      #报错

# list5 = ['张三','男',18,188.89,'陕西',True,99,1111,45.55,1111,'男','张三']
# print(list5)
# print(list5.pop())           #45.55
# print(list5)
# list5.pop(3)                 #188.89
# print(list5)
# list5.pop(-3)                #True
# print(list5)
# # list5.pop(-30)                #报错

# print(list5.remove('陕西'))          #None
# print(list5)
# list5.remove('张三')
# print(list5)
# # list5.remove('陕西')      #报错
# del list5[3]
# print(list5)
# list5.clear()
# print(list5)
# del list5
# print(list5)
#
# print(list5.index('陕西'))      #4
# # print(list5.index('陕西1'))     #报错
# print(list5.index('张三'))     #0
#
# nums = 0
# for i in list5:
#     if i == '张三':
#         nums += 1
# print(nums)
# print(list5.count('张三'))
#
# print('张三三' in ['张三三四',11,22])      #False
# print('张三三' in '张三三四')              #True

# list6 = [-11,29,12,30,90,0,5,40,11]
# print(list6)
# # 1)将list6中的所有元素从小到大排序
# list6.sort()                 #None
# print(list6)
# # 2)将list6中的所有元素从大到小排序
# list6.sort(reverse=True)
# print(list6)

list7 = [-11,29,22,30,19,0,5,40,11]
print(list7)
# # print(sorted(list7))
# # print(list7)
# # print(sorted(list7,reverse=True))
# # print(list7)
#
# list7.reverse()
# print(list7)
# list7.reverse()
# print(list7)
#
# print(list7[::-1])
# print(list7)

print(max(list7))           #40
print(max(list7[-4:]))      #40

print(min(list7))            #-11
print(min(list7[2:6:3]))     #0

print(sum(list7))           #145
print(sum(list7[3:]))       #105








# 练习1:用列表记录自己到过的8个不同的城市，城市名称由用户自行输入
'''
# 实现方式一： 使用for循环
citys = []
for i in range(8):      #i:0,1,2,3,4,5,6,7
    while True:
        #从键盘接收用户输入的一个城市
        chengshi = input(f'请输入第{i+1}个城市名称：')
    #判断该该城市尚未添加过，则将城市追加到citys列表中
        if chengshi not in citys:
            citys.append(chengshi)
            break
        else:
            print(f'{chengshi}已经输入过')
print(citys)

#实现方式二： 使用不定次循环
citys1 = []
while True:
    # 从键盘接收用户输入的一个城市
    chengshi = input(f'请输入第{len(citys1)+1}个城市名称：')
    #判断城市不存在与citys1中，则将其追加
    if chengshi not in citys1:
        citys1.append(chengshi)
    else:
        print(f'{chengshi}已经输入过')
    #判断城市满8个，则结束循环
    if len(citys1) == 8:
        break
print(citys1)
'''
# 练习2. 书店中对书价格进行调整, 现有列表如下:
# ['简爱 35.0元','飘 48.5元','鲁迅文集 158.0元','骆驼祥子 28.5元']
# 每本书价格均上涨3.5元,输出新的记录列表.
'''
# 实现方式一： 将处理的结果保存到一个新的列表中
book = ['简爱 35.0元','飘 48.5元','鲁迅文集 158.0元','骆驼祥子 28.5元']
book_new = []
#遍历book
for i in book:      #i:'简爱 35.0元','飘 48.5元','鲁迅文集 158.0元','骆驼祥子 28.5元'
    #取出原价格     '简爱 35.0元'-->'35.0'
    price = i[i.find(' ')+1:-1]
    #新价格=原价格+3.5     '35.0'-->'38.5'
    new_price = str(float(price)+3.5)
    #用新价格替换原价格，并将替换后的结果追加到新列表中
    book_new.append(i.replace(price,new_price))
#打印结果
print(book_new)

# 实现方式二： 直接在原列表上处理
book1 = ['简爱 35.0元','飘 48.5元','鲁迅文集 158.0元','骆驼祥子 28.5元']
for i in range(len(book1)):    #i:0,1,2,3
    # 取出原价格     '简爱 35.0元'-->'35.0'
    price = book1[i][book1[i].find(' ') + 1:-1]
    # 新价格=原价格+3.5     '35.0'-->'38.5'
    new_price = str(float(price) + 3.5)
    #用新价格替换原价格，并将替换后的结果重新赋给当前索引对应的元素(本质：修改当前元素)
    book1[i] = book1[i].replace(price,new_price)
print(book1)
'''









