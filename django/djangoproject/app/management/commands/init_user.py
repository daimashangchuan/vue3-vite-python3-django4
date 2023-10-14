from app.models import Users
import hashlib

# 创建新用户对象
user = Users.objects.create(
    name = "admin",
    phone = '18847139686',
    passWord = "123456",
    passWordMd5 = hashlib.md5(b'123456').hexdigest(),
    type = 1,
)

# 保存用户对象到数据库
user.save()
