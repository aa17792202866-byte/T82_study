# 面向对象题：
# 1. 创建一个名为User 的类，其中包含 姓first_name 和名last_name ，还有用户简介通常会存储的其他几个属性(例: 年龄,喜好等)。
#    在类User 中定义一个名为describe_user() 的方法，它打印用户信息摘要；
#    再定义一个名为greet_user() 的方法，它向用户发出个性化的问候。
#    创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。



class User:
    # 初始化方法
    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
    # 输出用户信息摘要
    def describe_user(self):
        print(f"{self.first_name}{self.last_name}的年龄是{self.age}岁，爱好是{self.hobby}")
    # 个性化问候
    def greet_user(self):
        print(f"你好，{self.first_name}{self.last_name}，欢迎使用本系统！")
# 创建用户对象
# user1 = User("张", "三", 20, "篮球")
# user2 = User("李", "四", 22, "编程")
# user3 = User("王", "五", 18, "音乐")
# # 调用方法
# user1.describe_user()
# user1.greet_user()
# print()
# user2.describe_user()
# user2.greet_user()
# print()
# user3.describe_user()
# user3.greet_user()
# 2. 定义一个学生类。
#   1）有下面的属性：
#      1. 姓名  2. 年龄  3.成绩(语文，数学，英语)[每课成绩的类型为整数]
#   2）类方法：
#       1.  获取学生的姓名：get_name() 返回类型:str
#       2.  获取学生的年龄：get_age() 返回类型:int
#       3.  返回3门科目中最高的分数。get_course() 返回类型:int
#       写好类以后，可以定义2个同学测试下:
#       例如：  zm = Student(‘zhangming’,20,[69,88,100])
#                  返回结果：zhangming 20 100
class Students:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def get_name(self):
        return str(self.name)
    def get_age(self):
        return int(self.age)
    def get_course(self):
        score = int(max(self.score))
        return score
# zm = Students("zhangming",20,[69,88,100])
# print(zm.name,zm.age,zm.score)
# ls = Students("lisi",18,[89,80,70])
# print(ls.name,ls.age,ls.score)


# 3. 定义一个学生类（父类）,父类的属性：姓名，性别，
#    再定义个子类，使得可以产生如下对象和使用方法:
#    李雷爱跑步，爱吃东西。
#    韩梅梅光爱跑步,不爱吃东西.
#    1）李雷体重75.0公斤
#    2）每次跑步会减肥0.5公斤
#    3）每次吃东西体重会增加1公斤
#    4）韩梅梅的体重是45.0公斤
#    5）韩梅梅每天跑步三回，吃东西一回
#    6）李雷每天跑步三回，吃东西吃五回
#   打印一天后，韩梅梅和李雷的体重分别是多少
# class StudentFather:
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender
# class StudentSon(StudentFather):
#     def __init__(self,paobu,chidongxi):
#         super().__init__(name,gender)
#         self.paobu = paobu
#         self.chidong = chidongxi
#     def fpaobu(self,paobu):


class StudentFather:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class StudentSon(StudentFather):
    def __init__(self, name, gender,paobu, chidongxi,weight):
        super().__init__(name, gender)
        self.paobu = paobu
        self.chidongxi = chidongxi
        self.weight = weight
    def fpaobu(self):
        self.weight -= 0.5
    def fchidongxi(self):
        self.weight += 1
    def dayin(self):
        return self.weight

li = StudentSon("李雷", "男", True, True,75)
for i in range(3):
    li.fpaobu()
for i in range(5):
    li.fchidongxi()
print(f"{li.name}一天后体重为{li.dayin()}")

hmm = StudentSon("韩梅梅", "女", True, False,45)
for i in range(3):
    hmm.fpaobu()
hmm.fchidongxi()
print(f"{hmm.name}一天后体重为{hmm.dayin()}")