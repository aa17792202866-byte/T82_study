# 数据库题：
# 1. 使用数据库,完成创建一张表,记录用户的姓名,卡号,余额.
import pymysql
con = pymysql.connect(host="localhost",port=3306,user="root",password="123456",database="ceshi",charset="utf8mb4", autocommit=True)
cu = con.cursor() #创建游标
sq1 = "create table if not exists user1 (id int unsigned primary key auto_increment,name varchar(10) not null,card varchar(12),amount DECIMAL(10, 2) NOT NULL DEFAULT 0.00 ) "
cu.execute(sq1)

#    1）表中插入一条开户数据,信息为 xiaoming,622778899000,1000
# sq2 = """insert into user1 values (0,"xiaoming","622778899000",1000);"""
# cu.execute(sq2)
#    2）用户xiaoming取了卡上200块
# sq3 = "update user1 set amount = amount - 200 where name = 'xiaoming';"
# cu.execute(sq3)
#    3）用户xiaoming查询自己的余额
# sq4 =  """ SELECT amount from user1 WHERE name = "xiaoming"; """
# cu.execute(sq4)
# res1 = cu.fetchone()
# print(res1)
#    4）用户xiaoming取完自己卡上的钱,进行销户
# sq5 = """DELETE FROM user1 where name = "xiaoming"; """
# cu.execute(sq5)
# 2. 一张表中保存的是各位同学的各科成绩（具体信息如下），要求必须写代码将表创建好，且用代码把每名学生的原始数据插入表中），编写程序计算出各位同学的总成绩每名同学的最后一列
#     a1 70 80 90
#     a2 80 85 95
#     a3 75 60 80
#创建表
# sq6 = """CREATE TABLE if not exists grades (id VARCHAR(5),class1 VARCHAR(3),class2 VARCHAR(3),class3 VARCHAR(3));"""
# cu.execute(sq6)
#插入数据
# sq7 = """INSERT INTO grades VALUES ("a1","70","80","90"),("a2","80","85","95"),("a3","75","60","80");"""
# cu.execute(sq7)
#最终
# sq8 = """select * from grades"""
# cu.execute(sq8)
# res5 = cu.fetchall()
# print(res5)
# zongchengji = []
# for i in res5:
#     sum2 = float(i[1]) + float(i[2]) + float(i[3])
#     print(sum2)
#     zongchengji.append(str(round(sum2,2)))
# print(zongchengji)
# # sq9 = """ALTER TABLE grades ADD avg VARCHAR(20) DEFAULT 0;"""   #新增字段
# # cu.execute(sq9)
# for j in range(len(zongchengji)):
#     sq10 = """UPDATE grades SET avg = %s WHERE id = %s"""
#     cu.execute(sq10, (zongchengji[j], res5[j][0]))
#最终

#失败了的
# for j in zongchengji:
#     a = zongchengji[-1]
#     sq10 = """update grades set avg=a where id = "a1" ;"""

# 3. 写程序实现创建一张表，表中有100行数据，数据内容为：
# 	name   ,  mailbox
#                vu1 , vu1@163.com
#                vu2,vu2@163.com
#                vu3,vu3@163.com
# 	……
#                ……
#        注：此题目分别使用for循环、存储过程两种方式实现
# sq1 = """CREATE TABLE IF NOT EXISTS user_mail (name VARCHAR(20),mailbox VARCHAR(50));"""
# cu.execute(sq1)
#
# pro_mailbox = "CREATE PROCEDURE proc_test()\n" \
#               "BEGIN\n" \
#               "    DECLARE i INT DEFAULT 1;\n" \
#               "    WHILE i < 101 DO\n" \
#               "        INSERT INTO user_mail(name, mailbox)\n" \
#               "        VALUES (CONCAT('vu', i), CONCAT('vu', i, '@163.com'));\n" \
#               "        SET i = i + 1;\n" \
#               "    END WHILE;\n" \
#               "END"
#
# cu.execute(pro_mailbox)
# cu.execute("CALL proc_test()")
#使用for循环实现
# for i in range(1, 101):
#     name = f"vu{i}"
#     mailbox = f"vu{i}@163.com"
#     cu.execute("INSERT INTO user_mail VALUES (%s, %s)",(name, mailbox))

#存储过程实现
# sq3 = """
# CREATE PROCEDURE add_users()
# BEGIN
#     DECLARE i INT DEFAULT 1;
#     WHILE i <= 100 DO
#         INSERT INTO user_mail(name, mailbox)
#         VALUES (
#             CONCAT('vu', i),
#             CONCAT('vu', i, '@163.com')
#         );
#         SET i = i + 1;
#     END WHILE;
# END
# """
# cu.execute(sq3)
# cu.execute("CALL add_users()")


# 列表题：
# 1. 写代码实现：将8名老师随机分配到3个办公室，要求：每个办公室不超过3个人
# a = ["a1","a2","a3","a4","a5","a6","a7","a8"]
# dict1 = {}
# office_num = 3
# import random
# if len(a) < office_num * 3:
#     for i in range(len(a)):
#         while 1: #定义不定次循环，这样就不会漏掉某个老师
#             jiaoshi = random.randint(1,office_num)
#             if jiaoshi not in dict1: #判断一下这个办公室是否出现过
#                 dict1[jiaoshi] = [] #新增一个办公室编号作为键，并加入个空列表
#             if len(dict1[jiaoshi]) < 3: #判断这个办公室的人数是否支持新增一个人
#                 dict1[jiaoshi].append(a[i]) #将字典中的列表新增一个人
#                 break #直到成功加入才跳出循环
#     dict1 = dict(sorted(dict1.items())) #将字典按照键值正序排序
#     for j in range(len(dict1)):
#         print(f"第{j+1}个办公室，共有{len(dict1[j+1])}个老师，分别是{dict1[j+1]}")
# else:
#     print("办公室数量不足以容纳所有老师")



"""
#笨办法
import random
a = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"]
random.shuffle(a)
dict1 = {1: a[0:3],2: a[3:6],3: a[6:8]}
print(dict1)
"""


"""
#笨办法改成聪明办法
import random
a = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"]
office_num = 3
max_people = 3
if len(a) <= office_num * max_people:
    random.shuffle(a)
    dict1 = {}
    for i in range(office_num):
        people = a[i * max_people : (i + 1) * max_people]
        if people:
            dict1[i + 1] = people
    print(dict1)
else:
    print("办公室数量不足以容纳所有老师")
"""

"""
#笨办法改成聪明办法但是不是很聪明
import random
a = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"]
office_num = 3
max_people = 3
# 先判断办公室够不够
if len(a) > office_num * max_people:
    print("办公室数量不足，无法完成分配")
else:
    random.shuffle(a)
    dict1 = {}
    avg = len(a) // office_num
    yu = len(a) % office_num
    # 随机选出哪些办公室多1个人
    more_office = random.sample(
        range(1, office_num + 1),
        yu
    )
    start = 0
    for i in range(1, office_num + 1):
        count = avg
        if i in more_office:
            count += 1
        dict1[i] = a[start:start + count]
        start += count
    print(dict1)
"""


# 2. 将列表[45,23,2,5,3,2,6,45,43,21,66,2,3,2]进行从小到大排序,不能用sorted()函数或list.sort()方法.
list2 = [45,23,2,5,3,2,6,45,43,21,66,2,3,2]
for i in range(len(list2)):
    for j in range(len(list2)):
        if list2[i] < list2[j]:
            list2[i],list2[j] = list2[j],list2[i]
print(list2)

list2 = [45, 23, 2, 5, 3, 2, 6, 45, 43, 21, 66, 2, 3, 2]

for i in range(len(list2)):
    for j in range(i + 1, len(list2)):
        if list2[i] > list2[j]:
            list2[i], list2[j] = list2[j], list2[i]

print(list2)
# 3. 用户输入任意字符串，判断是否存在第二大数字？有则打印，没有则打印-1
# s = input("请输入任意字符串：")

s = "adv123512"
nums = list(set([int(i) for i in s if i.isdigit()]))
if len(nums) < 2:
    print("-1")
else:
    nums.sort(reverse=True)
    print(f"第二大数字是{nums[1]}")

