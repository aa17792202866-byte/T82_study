changdu = int(input("请输入列表长度"))
list1 = []
list2 = []
for i in range(1,changdu+1):
    list1.append(i)
for i in range(changdu-1,0,-1):
    list2.append(i)
list1.extend(list2)
print(list1)