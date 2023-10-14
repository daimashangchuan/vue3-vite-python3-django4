import pymysql
pymysql.version_info = (1, 4, 6, "final", 0)  # 模拟 mysqlclient 版本信息
pymysql.install_as_MySQLdb()