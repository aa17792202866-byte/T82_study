list2 = [45, 23, 2, 5, 3, 2, 6, 45, 43, 21, 66, 2, 3, 2]

for i in range(1, len(list2)):
    temp = list2[i]      # 当前准备插入的数字
    j = i - 1

    # 前面的数字比 temp 大，就往右移动
    while j >= 0 and list2[j] > temp:
        list2[j + 1] = list2[j]
        j -= 1

    # 把 temp 放到合适的位置
    list2[j + 1] = temp

print(list2)