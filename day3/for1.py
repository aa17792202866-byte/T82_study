# print(list(range(1,10,1)))
#
# print(list(range(1,10,2)))

# 3.打印1 - 10之间所有的偶数(正序打) 2, 4, 6, 8, 10
print(list(range(2,11,2)))
# print(range(2,11,2))  #range(2, 11, 2)

# 4. 打印1-10之间所有的奇数(倒序打)
print(list(range(10,0,-1)))
for i in range (10,0,-1):
    if i % 2 == 1:
        print(i,end=" ")