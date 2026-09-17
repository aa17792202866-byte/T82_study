import pymysql

# 1. 建立数据库连接
con = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database="ceshi",
    charset="utf8mb4",  # 推荐使用 utf8mb4，支持更多字符集
    autocommit=True  # 加上这行，之后所有的增删改操作都会自动提交
)

# 2. 创建游标
cu = con.cursor()

try:
    # 3. 编写 SQL 语句：如果已存在 user 表则先删除（方便重复测试）
    cu.execute("DROP TABLE IF EXISTS `user`;")

    # 4. 编写创建 user 表的 SQL 语句
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS `user` (
        `id` INT AUTO_INCREMENT PRIMARY KEY COMMENT '用户ID',
        `username` VARCHAR(50) NOT NULL UNIQUE COMMENT '用户名',
        `password` VARCHAR(100) NOT NULL COMMENT '密码',
        `email` VARCHAR(100) DEFAULT NULL COMMENT '邮箱',
        `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """

    # 5. 执行创建表语句
    cu.execute(create_table_sql)
    print("user 表创建成功！")

    # 如果有写入/修改操作，建议提交事务
    con.commit()

except Exception as e:
    print("建表失败：", e)
    con.rollback()

finally:
    # 6. 关闭游标和数据库连接
    cu.close()
    con.close()
    print("数据库连接已关闭。")