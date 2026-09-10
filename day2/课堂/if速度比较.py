import timeit

# 第一种：先计算两个结果，再判断
code1 = """
res1 = num1 + num2
res2 = num1 - num2
if num1 < num2:
    result = res1
else:
    result = res2
"""

# 第二种：先判断，只计算需要的结果
code2 = """
if num1 < num2:
    result = num1 + num2
else:
    result = num1 - num2
"""

count = 1_000_000  # 每组执行 100 万次

# 分别测试小于、大于、等于三种情况
for num1, num2 in [(3, 5), (5, 3), (5, 5)]:
    setup = f"num1 = {num1}; num2 = {num2}"

    # 每种测 5 组，取最短时间，减少其他程序干扰
    t1 = min(timeit.repeat(code1, setup=setup, number=count, repeat=5))
    t2 = min(timeit.repeat(code2, setup=setup, number=count, repeat=5))

    print(f"\n输入：{num1} 和 {num2}")
    print(f"第一种执行 {count} 次：{t1:.6f} 秒")
    print(f"第二种执行 {count} 次：{t2:.6f} 秒")
    print(f"第二种耗时减少：{(t1 - t2) / t1:.2%}")
    print(f"平均每次节省：{(t1 - t2) / count * 1_000_000_000:.2f} 纳秒")