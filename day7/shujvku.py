import pymysql
import pymysql

print(pymysql.__version__)
con = pymysql.connect(host="localhost",port=3306,user="root",password="123456",database="ceshi",charset="utf8")
print(con)

import pymysql

# 1. 建立数据库连接
try:
    conn = pymysql.connect(
        host='localhost',       # 本地数据库地址，也可以写 '127.0.0.1'
        port=3306,              # MySQL默认端口号（整数）
        user='root',            # 数据库用户名
        password='123456',      # 数据库密码
        # database='your_db_name', # 可选：如果要直接指定要操作的数据库名，取消注释并填入数据库名
        charset='utf8mb4'       # 编码格式，推荐 utf8mb4 支持完整字符集（如 Emoji）
    )
    print("数据库连接成功！")

    # 2. 创建游标（用于执行 SQL 语句）
    cursor = conn.cursor()

    # 3. 执行测试查询（如查询 MySQL 版本）
    cursor.execute("SELECT VERSION();")
    result = cursor.fetchone()
    print("MySQL 版本:", result)

except pymysql.MySQLError as e:
    print("数据库连接失败：", e)

finally:
    # 4. 关闭资源（无论成功或失败都执行）
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn:
        conn.close()
    print("连接已关闭。")