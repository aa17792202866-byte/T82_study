def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    # 从中间分成两半
    mid = len(nums) // 2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    result = []

    i = 0
    j = 0

    # 比较左右两边最前面的数字
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 把剩下的加进去
    result.extend(left[i:])
    result.extend(right[j:])

    return result
list2 = [45, 23, 2, 5, 3, 2, 6, 45, 43, 21, 66, 2, 3, 2]
list2 = merge_sort(list2)
print(list2)