number = input("请输入一个非负整数：")
total = 0

for digit in number:
    total += int(digit)

print(f"各位数字之和是：{total}")

# 2. 计算一个任意5位正整数上的每位数字的立方和
