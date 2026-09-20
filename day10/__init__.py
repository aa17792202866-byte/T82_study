# class Person:
#     # 构造方法，创建对象时自动执行
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # 定义一个方法
#     def introduce(self):
#         print(f"我的名字是{self.name}，今年{self.age}岁")
#
#
# # 创建对象
# person1 = Person("张三", 20)
#
# # 调用方法
# person1.introduce()
#
# # 查看属性类型
# print(type(person1))
# print(type(person1.name))


class Person:

    def __init__(self,name, age):
        self.name = name
        self.age = age


p = Person("张三",20)
print(p.name)