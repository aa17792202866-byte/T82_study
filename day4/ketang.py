# 人与计算机玩猜数字的游戏，玩5次
# 其中：人猜的不在范围内不算次数
import random
cm_num = random.randint(1,100)
x=5
for i in range(0,x):
    while 1:
        hm_num = int(input("请输入1-100数字"))
        if 1 <= hm_num <= 100:
            if hm_num == cm_num:
                print("你猜对了")
            elif hm_num > cm_num:
                print("你猜大了")
            else:
                print("你猜小了")
            break
