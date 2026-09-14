# 4. 书店中对书价格进行调整, 现有列表如下:
# ['简爱 35.0元','飘 48.5元','鲁迅文集 158.0元','骆驼祥子 28.5元']
# 每本书价格均上涨3.5元,输出新的记录列表.
list1 = ['简爱 35.0元','飘 48.5元','鲁迅文集 158.0元','骆驼祥子 28.5元']
# l1 = list1[0]
# print(l1.find(" "))
# print(l1.find("元"))
# print(l1[3:7])
# print(float(l1[3:7])+3.5)

# for i in range(len(list1)):
#     l1 = list1[i]
#     shou = l1.find(" ")
#     wei = l1.find("元")
#     print(l1[shou+1:wei])
#     print(float(l1[shou+1:wei])+3.5)

# 练习3:用列表记录自己到过的8个城市:
citys = ["baoji","xian","zhengzhou","shanghai","taiyuan","suzhou","hangzhou","nanjing","nanjing"]
# 1)增加一个城市"北京"
citys.append("beijing")
print(citys)
# 2)判断是否有城市"南京",如果有,删除
for i in range(len(citys)-1,-1,-1):
    if citys[i] == "nanjing":
        citys.remove("nanjing")
print(citys)

# citys = [c for c in citys if c != "nanjing"]
# print(citys)

# while "nanjing" in citys:
#     citys.remove("nanjing")
# print(citys)
# 3)判断索引为3的城市是否为'东京',如不是把索引为3的城市修改为"东京"
# for i in range(len(citys)):
#     if citys[3] != "dongjing":
#         citys[3] = "dongjing"
# print(citys)
# 4)打印出每一个城市
# print(citys)
# # 5)利用切片,切出来前五个城市.
# print(citys[:5])




