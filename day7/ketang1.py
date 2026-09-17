# 3. 将[2,34,56,35,21,33,25,66]列表中大于等于37的元素作为键，该元素减去10的结果作为值，保存到一个字典中
list3 = [2,34,56,35,21,33,25,66]
dict3 = {}
for i in list3:
    if i >= 37:
        dict3[i] = i-10
print(dict3)

dict4 = {i:i-10 for i in list3 if i >= 37}
print(dict3)