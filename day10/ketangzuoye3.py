# class A:
#     def test(self):
#         print("A")
#
#
# class B:
#     def test(self):
#         print("B")
#
#
# class C(A, B):
#     pass
#
#
# c = C()
# c.test()

try:
    a = int(input())
    b = int(input())

    print(a / b)

except ValueError:
    print("请输入整数")

except ZeroDivisionError:
    print("除数不能为0")

except Exception as e:
    print("未知错误:", e)