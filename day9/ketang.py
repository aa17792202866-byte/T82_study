#以只读模式打开
# f1 = open("123.txt",mode="r",encoding="utf-8")
# print(f1)
# print(f1.read())
# f1.close()

#以写入模式打开
# f2 = open("123.txt",mode="w+",encoding="utf-8")
# print(f2.read())
# f2.write("123")
# f2.close()

# 以可读写（清空）模式打开
f2 = open("123.txt", mode="w+", encoding="utf-8") #[cite: 7]

# 1. 先写入内容
f2.write("123456789我\n87654321") #[cite: 7]

# 2. 将文件指针重置到开头（关键点！）
f2.seek(0)
con = f2.read() #[cite: 7]
# print(f2.tell())
nums = len(con) - con.count(' ') - con.count('\n')
print(nums)
# 3. 再读取并打印
# print(f2.read(3)) #[cite: 7]
# print(f2.tell())
# print(f2.read()) #[cite: 7]
# print(f2.tell())
#
# f2.seek(0)
# print(f2.tell())
# print(f2.read())
# print(f2.tell())
# 4. 关闭文件
f2.close() #[cite: 7]