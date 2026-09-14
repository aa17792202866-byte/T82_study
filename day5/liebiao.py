li = ['taibai','alexC','AbC','egon','Ritian','Wusir','aqc']
# 1) 计算列表长度并输出
print(len(li))
# 2）向列表中追加一个元素并输出最终列表
li.append("nihao")
print(li)
# 3）在指定位置1插入元素ttt
li.insert(1,"ttt")
print(li)
# 4）修改指定元素‘AbC’为‘ooo’
li[3]="ooo"
print(li)

s1 = li.index('ooo')
print(s1)
li[li.index('ooo')]='韩瑞轩'
print(li)
# 练习3:用列表记录自己到过的8个不同的城市，城市名称由用户自行输入
# chengshi = []
# for i in range(8):
#     while 1:
#         s = input("请输入城市名称")
#         if s not in chengshi:
#             print("录入成功")
#             chengshi.append(s)
#             break
#         else:
#             print("已重复，请重新输入")
# # print(f"所有的城市分别为{chengshi}")
# print(f"所有的城市分别为{' '.join(chengshi)}")