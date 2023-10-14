# mysql

## 数据库忘记密码
```
需要关闭数据库服务
修改配置  进入无密码设置
  cd mysql/my.ini  添加
  skip-grant-tables=1
开启数据库服务
mysql -u root -p
重新填写密码

关闭数据库服务
修改配置  取消无密码设置
mysql -u root -p  
新密码

```



## 账户
###  创建账户
```
% 符号表示允许从任何主机连接。如果您希望限制连接的主机，可以替换为具体的主机名或IP地址

CREATE USER '用户名'@'%' IDENTIFIED BY '密码';
CREATE USER '用户名'@'hostname' IDENTIFIED BY '密码';
```

### 删除账户
```
DROP USER '用户名'@'%';
drop user '用户名'@'localhost';
```

### 修改用户名的密码
```
修改用户名和密码需要具备足够的权限才能执行
ALTER USER '用户名'@'%' IDENTIFIED BY '新密码';
alter user '用户名'@'%' identified by '新密码';
```

### 查询用户
```
查询所有用户名和密码和权限（需要权限）
SELECT User, Host, Password FROM mysql.user;

查看特定用户的权限信息
SHOW GRANTS FOR 'username'@'hostname';
show grants for '用户名'@'hostname';

查询当前登录的用户
SELECT CURRENT_USER(); 
select current_user()
查询当前用户的详细信息，包括用户名、主机、密码和权限等
SELECT USER(), CURRENT_USER(), CURRENT_USER as 'Logged-in User', SUBSTRING_INDEX(USER(), '@', -1) as 'Host';

```

### 给用户设置数据库权限
```
* 代表数据库所有的表
GRANT 权限 ON 数据库.表名,数据库.表名,数据库.*  TO 'username'@'hostname';

权限列表
  SELECT：允许查询表中的数据。
  INSERT：允许向表中插入数据。
  UPDATE：允许更新表中的数据。
  DELETE：允许删除表中的数据。
  CREATE：允许创建新的表或数据库。
  DROP：允许删除表或数据库。
  ALL PRIVILEGES：允许所有操作权限。

```


## 数据库

### 查看所有数据库
```
show databases;
```
### 创建数据库
```
create database <数据库名>;
create database <数据库名> DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
CREATE DATABASE mydatabase  CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
数据库名为 mydatabase 使用了字符集为 utf8mb4，排序规则为 utf8mb4_general_ci。
```
### 进入数据库
```
use <数据库名>;
```
### 查看当前数据库
```
select database();
```
### 删除数据库
```
drop database <数据库名>;
```



## 表

### 查看所有表
```
show tables;
查看表的字段结构
desc 表名;

```
### 新增表
```
新增表和列
  create table 表名; (
    column1 datatype
  )
```

### 删除表 
#### 删除单个表
```
drop table 表名;
```
#### 删除数据库所有的表
```
  SET FOREIGN_KEY_CHECKS = 0;  -- 可能需要在执行 DROP TABLE 前禁用外键约束
  DROP TABLE table1, table2, ...;  -- 将 table1, table2 替换为实际的表名
  SET FOREIGN_KEY_CHECKS = 1;  -- 可能需要在执行 DROP TABLE 后重新启用外键约束

  SET FOREIGN_KEY_CHECKS = 0; -- 禁用外键检查，以防有外键约束
  SET @tables = NULL;
  SELECT GROUP_CONCAT(table_name) INTO @tables
  FROM information_schema.tables
  WHERE table_schema = DATABASE();
  SET @tables = CONCAT('DROP TABLE IF EXISTS ', @tables);
  PREPARE stmt FROM @tables;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;
  SET FOREIGN_KEY_CHECKS = 1; -- 启用外键检查
```


### 修改表
```
修改表名
  alter table 旧表名 rename to 新表名;
  ALTER TABLE 旧表名 RENAME TO 新表名;

修改表的列名
  alter table 表名 rename column 旧列名 to 新列名,
  ALTER TABLE table_name RENAME COLUMN current_column_name TO new_column_name;

修改表的列名
  ALTER TABLE table_name 
    CHANGE column1 current_column1_name new_column1_name column1_data_type, 
    CHANGE column2 current_column2_name new_column2_name column2_data_type,
    ...
  alter table 表名 change 旧列名 旧列名 新列名 新类型, 旧列名 旧列名 新列名 新类型
```

### 查询
```
查看所有表
  show tables; 

查看表的内部信息
  desc table 表名 
```



## 数据
```
查看表内所有的数据
  select * from 表名
```






