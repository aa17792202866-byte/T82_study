# 1.设计一个工资类(Salary)，其中的数据成员有：
# salary_al代表所有员工工资;
# 整型值number表示的在职工人数。
#
# 调用你自己设计好的成员函数完成下面的功能：
# 1). 输入职工工资，工资保存到salary_al列表中，实际人数保存到number中（输入-1标志着工资输入结束）；
# 2). 给每个人涨300元工资；
# 3). 对涨后的工资进行排序；
# 4）输出排序后的工资
# class Salary:
#     def __init__(self,salary_al,number):

class Salary:

    # 构造方法，初始化成员变量
    def __init__(self):
        self.salary_al = []   # 保存员工工资
        self.number = 0       # 员工人数


    # 输入员工工资
    def input_salary(self):
        while True:
            salary = int(input("请输入员工工资(-1结束)："))

            if salary == -1:
                break

            self.salary_al.append(salary)
            self.number += 1


    # 每个人涨300元
    def add_salary(self):
        for i in range(self.number):
            self.salary_al[i] += 300


    # 工资排序
    def sort_salary(self):
        self.salary_al.sort()


    # 输出工资
    def show_salary(self):
        print("员工人数：", self.number)
        print("排序后的工资：", self.salary_al)



# 创建对象
salary = Salary()

# 输入工资
salary.input_salary()

# 涨工资
salary.add_salary()

# 排序
salary.sort_salary()

# 输出
salary.show_salary()