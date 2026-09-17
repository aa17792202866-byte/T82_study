# 1. 用一个字典来记录学生的一系列信息,包括: 姓名,性别,年龄,身高,体重信息
# xuesheng = {"name":"张三","sex":"男","age":18,"height":180.2,"weight":80.5}
# print(xuesheng)
# # 1)请在字典中增加一个键值对,"sid":"stu001"，输出添加后的字典
# xuesheng["sid"] = "stu001"
# print(xuesheng)
# # 2)请删除字典中键为age的元素,并输出删除后的结果
# xuesheng.pop("age")
# print(xuesheng)
# # 3)请获取字典中"name"对应的值
# print(xuesheng.get("name"))
# # 4）统计字典的长度
# print(len(xuesheng))

# 2. 循环录入5名同学的信息并保存，每名同学的信息均包含：姓名、性别、年龄、手机号
for i in range(1,6):
    s = {"name":"","sex":"","age":"","phone":""}
    name = input(f"请输入第{i}个学生姓名：")
    sex = input(f"请输入第{i}个学生性别：")
    age = input(f"请输入第{i}个学生年龄：")
    phone = input(f"请输入第{i}个学生手机号：")
    s["name"] = name
    s["sex"] = sex
    s["age"] = age
    s["phone"] = phone
    if i == 1:
        s1 = s
    if i == 2:
        s2 = s
    if i == 3:
        s3 = s
    if i == 4:
        s4 = s
    if i == 5:
        s5 = s
print(s1,s2,s3,s4,s5,sep="\n")



