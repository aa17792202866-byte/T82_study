'''
for循环的嵌套：
for循环里面的功能代码还是for循环

执行顺序：
新进外循环，再进内循环，待内循环跑完后再执行下次外循环
'''
'''
# 例1：
for i in range(2):         #外循环 i:[0,1]
    for j in range(2):     #内循环 j:[0,1]
        print(i,j,sep='',end=' ')
#00 01 10 11
'''
'''
# 例2：
for i in range(2):         #外循环 i:[0,1]
    print(i,end='')
    for j in range(2):     #内循环 j:[0,1]
        print(j,end='')
    print(end=' ')
#001 101
'''
'''
# 例3:
for i in range(2):             #外循环 i:[0,1]
    for j in range(2):         #j:[0,1]
        for x in range(2):     #x:[0,1]
            print(i,j,x,sep='',end=' ')
#000 001 010 011 100 101 110 111
'''
# 例4： 打印如下图形
# * * * * *
'''
# 笨办法：
print('* * * * * ')
print('* '*5)
#使用for循环
for i in range(5):
    print('* ',end='')
'''
# 例5：打印如下图形
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
'''
for i in range(5):    #外循环：控制行
    #每行打印5个星空
    for j in range(5):
        print('* ', end='')
    #换行
    print()
'''

# 例6：打印如下图形
# *
# * *
# * * *
# * * * *
# * * * * *
'''
for i in range(1,6):     #控制行：i:[1,2,3,4,5]
    #每行打印星空的数量与当前行的行号相同
    for j in range(i):      
        print('* ',end='')
    #换行
    print()
 '''

# 例7：打印九九乘法表
for i in range(1,10):        #控制行：i:[1,2,3,4,5,6,7,8,9]
    #每行打印星空的数量与当前行的行号相同
    for j in range(i):       #控制列
        print(f'{j+1}x{i}={(j+1)*i}\t',end='')
    #换行
    print()

for i in range(1,10):        #控制行：i:[1,2,3,4,5,6,7,8,9]
    #每行打印星空的数量与当前行的行号相同
    for j in range(1,i+1):       #控制列
        print(f'{j}x{i}={j*i}\t',end='')
    #换行
    print()












