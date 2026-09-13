
a = int(input("请输入题目:"))
print(f"题目{a}")
if(a == 1):
    print("1. 循环输入7天温度，求平均温度")
    print("代码=================")
    daima = '''
    he = 0 ;
    for i in range(1,8,1):
        print(f'请输入第{i}天的温度:')
        wen_du = float(input(""))
        he = he + wen_du
    avg = he / 7
    print('7天的平均温度为%.2f'%avg)
    '''
    print(daima)
    print("执行程序================================")
    he = 0 ;
    for i in range(1,8,1):
        print(f'请输入第{i}天的温度:')
        wen_du = float(input(""))
        he = he + wen_du
    avg = he / 7
    print('7天的平均温度为%.2f'%avg)
elif(a==2):
    print("求 100-200以内同时能被7、8整除的数，并统计个数\n答案为：")
    print("代码=================")
    daima = '''
        j = 0
        STR = ''
        for i in range(100,201,1):
        if i%7==0 and i%8==0:
            STR = str(i) + ' ' + STR
            j += 1
        print(f'100-200以内同时能被7、8整除的数为{STR} \n统计个数{j}')
        '''
    print(daima)
    print("执行程序================================")
    j = 0
    STR = ''
    for i in range(100,201,1):
        if i%7==0 and i%8==0:
            STR = str(i) + ' ' + STR
            j += 1
    print(f'100-200以内同时能被7、8整除的数为{STR} \n统计个数{j}')
elif(a == 3):
    print("求同时能被2、3、5整除的第一个三位正整数")
    print("代码=================")
    daima = '''
            i = 1
            while 1:
            if i%2==0 and i%3==0 and i%5==0:
                print(f'同时能被2、3、5整除的第一个三位正整数为{i}')
                break;
            i+=1
            '''
    print(daima)
    print("执行程序================================")
    i = 1
    while 1:
        if i%2==0 and i%3==0 and i%5==0:
            print(f'同时能被2、3、5整除的第一个三位正整数为{i}')
            break;
        i+=1
elif(a == 4):
    print("求 0 -1 + 2 - 3 + 4 - 5 + 6 -7.... + 100 的结果")
    print("代码=================")
    daima = '''
                he = 0
                hehe = 0
                for i in range(0,101,1):
                    if(i % 2 == 0):
                    he = he + i
                else:
                    hehe += i
                print(f'0 -1 + 2 - 3 + 4 - 5 + 6 -7.... + 100 的结果为{he-hehe}')
                '''
    print(daima)
    print("执行程序================================")
    he = 0
    hehe = 0
    for i in range(0,101,1):
        if(i % 2 == 0):
            he = he + i
        else:
            hehe += i
    print(f'0 -1 + 2 - 3 + 4 - 5 + 6 -7.... + 100 的结果为{he-hehe}')
elif(a == 5):
    print("从键盘接收用户输入的自己最喜欢的歌手姓名（一次输入一名歌手信息即可），直到用户不想输入了（输入'q'退出）：")
    print("代码=================")
    daima = '''
                    print("请输入您最喜欢的歌手名字：(按q可退出)")
                    i = 1
                    while 1:
                    name = input()
                    if(name == 'q'):
                        print("退出成功")
                        break;
                    else:
                    #保证一次只输入一个名字
                    i+=1
                    print(f"请输入您第{i}喜欢的歌手名字：")
                    '''
    print(daima)
    print("执行程序================================")
    print("请输入您最喜欢的歌手名字：(按q可退出)")
    i = 1
    while 1:
        name = input()
        if(name == 'q'):
            print("退出成功")
            break;
        else:
            #保证一次只输入一个名字
            i+=1
            print(f"请输入您第{i}喜欢的歌手名字：")

elif(a == 6):
    print("小明家有一只乌龟,每天吃一根火腿肠,冰箱中有70根火腿肠,吃光所有的火腿肠需要几周?打印一周后冰箱中还剩多少根火腿肠,二周后?三周后?四周后?...直到最后一周?强制要求：使用不定次循环实现，小明家冰箱的火腿肠根数可以随意给定，不一定非得是70按周计算、不用按天计算")
    print("代码=================")
    daima = '''
    i = 1
    while 1:
        print(f'{i}周后还有{70-i*7}根')
        if(70- i*7 == 0):
            break
        i += 1
                        '''
    print(daima)
    print("执行程序================================")
    i = 1
    while 1:
        print(f'{i}周后还有{70-i*7}根')
        if(70- i*7 == 0):
            break
        i += 1
elif(a == 7):
    print("Chuckie Lucky赢了100W美元，他把它存入一个每年盈利8%的账户。在每年的最后一天，Chuckie取出10W美元。打印每年他的剩余金额,直至0为止, 打印多少年后Chuckie会清空他的账户。\n答案为：")
    print("代码=================")
    daima = '''
    money = 100
    year = 0
    while 1:
        money = money * 1.08 - 10
        if money < 0:
            print(f"{year + 1}年后Chuckie会清空他的账户。")
            break
        else:
            year += 1
                            '''
    print(daima)
    print("执行程序================================")
    money = 100
    year = 0
    while 1:
        money = money * 1.08 - 10
        if money < 0:
            print(f"{year + 1}年后Chuckie会清空他的账户。")
            break
        else:
            year += 1
elif(a == 8):
    print("依次输入几个数据，直到0作为输入的结束，然后求出输入的这些数据的总和及平均值（0不算次数）\n答案为：")
    print("代码=================")
    daima = '''
    he = 0
    x = 1
    cishu = 0
    while 1:
        if x == 0:
            cishu -= 1
            break
        else:
            x = int(input("请输入数字:"))
            cishu += 1
            he += x
            avg = he / cishu
    print(f'这些数据的总和:{he}及平均值:{cishu}')
                               '''

    print(daima)
    print("执行程序================================")
    he = 0
    x = 1
    cishu = 0
    while 1:
        if x == 0:
            cishu -= 1
            break
        else:
            x = int(input("请输入数字:"))
            cishu += 1
            he += x
            avg = he / cishu
    print(f'这些数据的总和:{he}及平均值:{cishu}')
elif(a == 9):
    print(". 有一张厚度为0.1毫米的纸，假设它足够大，重复将其对折，问对折多少次之后，其厚度可以抵达（再对折一次就超过）珠穆朗玛峰的高度？珠峰高度统一为8844.32米\n答案为：")
    print("代码=================")
    daima = '''
    x = 0.1
    cishu = 0
    while x <= 8848.32 * 1000:
        x = x*2
        cishu+=1
    print(f"对折{cishu-1}次之后，其厚度可以抵达（再对折一次就超过）珠穆朗玛峰的高度")
                                  '''

    print(daima)
    print("执行程序================================")
    x = 0.1
    cishu = 0
    while x <= 8848.32 * 1000:
        x = x*2
        cishu+=1
    print(f"对折{cishu-1}次之后，其厚度可以抵达（再对折一次就超过）珠穆朗玛峰的高度")

elif(a == 10):
    print("有一个10米深的井，井底有只青蛙，青蛙每次向上爬5米后就会下滑3米，设计一个程序计算青蛙需要几次能爬到井外")
    print("代码=================")
    daima = '''
    i = 1
    j = 0
    while 1:
        j += 5
        if j <= 10 :
            i += 1
            j -= 3
        else:
            print(f"青蛙需要{i}次能爬到井外")
            break
                                      '''
    print(daima)
    print("执行程序================================")
    i = 1
    j = 0
    while 1:
        j += 5
        if j <= 10 :
            i += 1
            j -= 3
        else:
            print(f"青蛙需要{i}次能爬到井外")
            break
else:
    print("总共是10个题目，请输入正确题目序号")



















