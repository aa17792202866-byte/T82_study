def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):          # 外层循环：共 n-1 轮
        for j in range(n - 1 - i):  # 内层循环：每轮比较次数递减
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 交换相邻元素
    return arr

# 测试
data = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(data))  # [11, 12, 22, 25, 34, 64, 90]
