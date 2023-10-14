# API

## 接口详情

    说明: 接口前缀为统一的 /api

    接口格式
      参数
        参数名[T]:类型 说明   T必传
      {
        "code": 状态码,     0成功  1后端代码问题  其他状态浏览器或者参数方式问题
        "msg":  错误信息,
        "body": 返回信息
      }

## 修订历史

```
一: 20230614 -- 孙继伟
```

### 后台管理端

### 登录/退出/个人信息

#### 登录接口

```
  URL: /login

  请求方式: post

  参数:
    phone[T]:  string   登录账户
    passWord[T]:  string   登录密码
    passWordMd5[T]:  string  加密

  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": {
        token             认证token  需要放到 cookit
        name              姓名
        gender:int       性别（1男，2女）
        age:int          年龄
        phone             手机号
        address           地址
        permission        权限列表  "[{ path:路由,title:标题,icon:图表,name:名称,component:文件位置 }]"
        roleId:int       用户角色
        createTime        创建时间
        updataTime        修改时间
      }
    }
```

#### 退出接口

```
  URL: /logout

  请求方式: get

  参数:

  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": null
    }
```

#### 获取个人信息

```
  URL: /userInfo/detail

  请求方式: get

  参数:

  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": {
        token             认证token  需要放到 cookit
        name              姓名
        gender: int       性别（1男，2女）
        age:int           年龄
        phone             手机号
        address           地址
        permission        权限列表  "[{ path:路由,title:标题,icon:图表,name:名称,component:文件位置 }]"
        roleId: int       用户角色
        createTime        创建时间
        updataTime        修改时间
      }
    }
```

#### 编辑个人信息

```
  URL: /userInfo/updata

  请求方式: post

  参数:
    passWord[T]          密码
    phone[T]             手机号
    name              姓名
    gender: int       性别（1男，2女）
    age:int           年龄
    address           地址
    roleId: int       用户角色

  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": {
        token             认证token  需要放到 cookit
        name              姓名
        gender: int       性别（1男，2女）
        age:int           年龄
        phone             手机号
        address           地址
        permission        权限列表  "[{ path:路由,title:标题,icon:图表,name:名称,component:文件位置 }]"
        roleId: int       用户角色
        createTime        创建时间
        updataTime        修改时间
      }
    }
```



### 用户模块

#### 添加用户

```
  URL: /user/insert

  请求方式: post

  参数:
    phone[T]             手机号
    name              姓名
    gender: int       性别（1男，2女）
    age:int           年龄
    address           地址
    roleId: int       用户角色

  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": {
        id
        name              姓名
        gender: int       性别（1男，2女）
        age:int           年龄
        phone             手机号
        address           地址
        roleId: int       用户角色
        createTime        创建时间
        updataTime        修改时间
      }
    }
```

#### 删除用户

```
  URL: /user/delete

  请求方式: delete

  参数:
    id[T]:  int

  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": null
    }
```

#### 编辑用户信息

```
  URL: /user/updata

  请求方式: put

  参数:
    id[T]: int
    phone[T]             手机号
    name              姓名
    gender: int       性别（1男，2女）
    age:int           年龄
    address           地址
    roleId: int       用户角色

  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": {
        id
        name              姓名
        gender: int       性别（1男，2女）
        age:int           年龄
        phone             手机号
        address           地址
        roleId: int       用户角色
        createTime        创建时间
        updataTime        修改时间
      }
    }
```

#### 用户列表

```
  URL: /user/list

  请求方式: get

  参数:
    keyword         关键字搜索
    page            当前页数
    pageSize        一页多少条
  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": {
        total           总条数
        pageCount       总页数
        page            当前页数
        pageSizes        一页多少条
        list: [
          {
            id
            name              姓名
            gender: int       性别（1男，2女）
            age:int           年龄
            phone             手机号
            address           地址
            roleId: int       用户角色
            createTime        创建时间
            updataTime        修改时间
          }
        ]
      }
    }
```

#### 用户详情 一条

```
  URL: /user/detail

  请求方式: get

  参数:
    id[T]: int

  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": {
        id
        name              姓名
        gender: int       性别（1男，2女）
        age:int           年龄
        phone             手机号
        address           地址
        roleId: int       用户角色
        createTime        创建时间
        updataTime        修改时间
      }
    }
```



### 角色模块

#### 添加角色

```
  URL: /role/insert

  请求方式: post

  参数:
    name[T]          角色名称
    detail             角色说明
    permission       权限列表


  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": {
        id
        name[T]          角色名称
        detail             角色说明
        permission       权限列表
      }
    }
```

#### 删除角色

```
  URL: /role/delete

  请求方式: delete

  参数:
    id[T]:  int

  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": null
    }
```

#### 编辑角色

```
  URL: /role/updata

  请求方式: put

  参数:
    id[T]: int
    name[T]          角色名称
    detail             角色说明
    permission       权限列表

  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": {
        id[T]: int
        name[T]          角色名称
        detail             角色说明
        permission       权限列表
      }
    }
```

#### 角色列表

```
  URL: /role/list

  请求方式: get

  参数:
    keyword         关键字搜索
    page            当前页数
    pageSize        一页多少条
  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": {
        total           总条数
        pageCount       总页数
        page            当前页数
        pageSizes        一页多少条
        list: [
          {
            id
            name[T]          角色名称
            detail             角色说明
            permission       权限列表
          }
        ]
      }
    }
```

#### 用户详情 一条

```
  URL: /user/detail

  请求方式: get

  参数:
    id[T]: int

  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": {
        id
        name[T]          角色名称
        detail             角色说明
        permission       权限列表
      }
    }
```



### 通知模块

#### 添加通知

```
  URL: /notice/insert

  请求方式: post

  参数:
    name[T]          通知标题
    detail             通知详情

  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": {
        id
        name[T]          通知标题
        detail             通知详情
      }
    }
```

#### 删除角色

```
  URL: /notice/delete

  请求方式: delete

  参数:
    id[T]:  int

  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": null
    }
```

#### 编辑角色

```
  URL: /notice/updata

  请求方式: put

  参数:
    id[T]: int
    name[T]            通知标题
    detail             通知详情

  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": {
        id[T]: int
        name[T]           通知标题
        detail            通知详情
      }
    }
```

#### 角色列表

```
  URL: /notice/list

  请求方式: get

  参数:
    keyword         关键字搜索
    page            当前页数
    pageSize        一页多少条
  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": {
        total           总条数
        pageCount       总页数
        page            当前页数
        pageSizes        一页多少条
        list: [
          {
            id
            name[T]          通知标题
            detail             通知详情
          }
        ]
      }
    }
```

#### 用户详情 一条

```
  URL: /notice/detail

  请求方式: get

  参数:
    id[T]: int

  返回:
    {
      "code": 0,
      "msg":  "操作成功！",
      "body": {
        id
        name[T]          通知标题
        detail             通知详情
      }
    }
```

