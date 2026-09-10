try:
    score = int(input("请输入学生的分数："))
except ValueError:
    print("输入无效，请输入整数分数！")
    exit()

if score < 0 or score > 100:
    print("分数超出范围（0~100）！")
else:
    if score >= 90:
        print("优秀")
    elif score >= 80:
        print("中")
    elif score > 60:
        print("一般")
    else:
        print("不及格")
