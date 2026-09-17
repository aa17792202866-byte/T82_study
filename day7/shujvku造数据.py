import pymysql

# 1. 建立连接
con = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database="ceshi",
    charset="utf8mb4"
)

cu = con.cursor()

# 2. 准备要插入的多条测试数据 (用户名, 密码, 邮箱)
users_data = [
    ('熊大', '123456', 'xiongda@qq.com'),
    ('熊二', '654321', 'xionger@163.com'),
    ('光头强', 'admin123', 'guangtouqiang@gmail.com'),
    ('吉吉国王', 'jiji888', 'jiji@qq.com'),
    ('毛毛', 'maomao666', 'maomao@163.com')
]

# 3. 编写安全的 SQL 占位符语句（%s 防 SQL 注入）
sql = "INSERT INTO `user` (`username`, `password`, `email`) VALUES (%s, %s, %s);"

try:
    # 4. 使用 executemany 批量插入数据
    cu.executemany(sql, users_data)

    # 5. 【关键】手动提交事务，数据才会真正写入数据库
    con.commit()
    print(f"成功造入 {cu.rowcount} 条用户测试数据！")

except Exception as e:
    # 如果出错则回滚，防止脏数据
    con.rollback()
    print("数据写入失败，已回滚：", e)

finally:
    cu.close()
    con.close()