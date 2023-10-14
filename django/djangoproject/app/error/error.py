
ERROR_CODE_1100 = 1100
ERROR_CODE_1200 = 1200
ERROR_CODE_1300 = 1300

ERROR_CODE_1400 = 1400

ERROR_CODE_1600 = 1600  # 认证失败


class ErrorMsg:
    MSG_1100 = "缺少必要参数！"

# 公共
class CommonError:
    MSG_1200 = "账号或密码错误！"
    MSG_1300 = "用户信息不存在！"
    MSG_1400 = "当前账号权限不够！"
    MSG_1600 = "认证失败！"


# 角色模块
class RoleError:

    MSG_1200 = "角色名称已存在！"
    MSG_1300 = "角色不存在！"

# 账号
class UserError:

    MSG_1200 = "账户已存在！"
    MSG_1300 = "账户不存在！"
    

# 通知管理
class NoticeError:

    MSG_1200 = "通知标题已存在！"
    MSG_1300 = "数据不存在！"

