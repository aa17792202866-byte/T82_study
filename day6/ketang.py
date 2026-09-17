# 2. 求100以内含6的数
list1 = []
for i in range(1,101):
    if "6" in str(i):
        list1.append(i)
print(list1)

list2 = [i for i in range(1,101) if "6" in str(i)]
print(list2)

 # 3. 计算1-100之间除了30,60,90之外的和
list3 = []
for i in range(1,101):
    if i not in (30,60,90) :
        list3.append(i)
print(sum(list3))

list4 = [i for i in range(1,101) if i not in (30,60,90)]
print(sum(list4))