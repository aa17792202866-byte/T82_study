def my_find(mystr, str_to_find, start=0, end=None):
    # 处理默认的结束位置 end
    if end is None:
        end = len(mystr)

    # 处理边界情况：起点或终点超出范围
    start = max(0, start)
    end = min(len(mystr), end)

    target_len = len(str_to_find)

    # 查找的子串为空时，直接返回起始位置
    if target_len == 0:
        return start if start <= end else -1

    # 在指定范围内滑动对比
    # end - target_len + 1 是为了防止指针越界
    for i in range(start, end - target_len + 1):
        # 截取与目标等长的子串进行对比
        if mystr[i: i + target_len] == str_to_find:
            return i  # 找到匹配，立即返回匹配首字符的索引

    return -1  # 找遍了指定的范围都没找到，返回 -1
s = "abcdefsdsadabcsadabccabcczabczccabczxzabczxdaabcadabcabc"
count = 0
index = 0

while True:
    index = my_find(s, "abc", index)  # 调用你自定义的 my_find
    if index == -1:
        break
    count += 1
    index += 3  # 跳过刚找到的 "abc" 的长度

print("出现总次数:", count)