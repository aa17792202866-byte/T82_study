# 1. 创建一个猫类，要求有姓名、品种、年龄、毛色的属性，有吃、睡、抓老鼠的行为；并调用该类创建3个不同的对象
class Cat:
    def __init__(self,name,variety,age,color):
        self.name = name
        self.variety = variety
        self.age = age
        self.color = color
    #定义吃的方法
    def eat(self,bowls):
        print(f"{self.name}一天能吃{bowls}只老鼠")
    def sleep(self,hour):
        print(f"{self.name}一天能睡{hour}小时")
    def zhua(self,bowls):
        print(f"{self.name}一天能抓{bowls}只老鼠")
a = Cat("tom","nainiu",5,"white")
b = Cat("tom1","nainiu1",6,"black")
c = Cat("tom2","nainiu2",7,"green")
print(a.name,type(a.name))
a.name = "tom4"
print(a.name)
b.variety = "buou"
c.age = 100
print(b.variety,c.age)
a.eat(5)