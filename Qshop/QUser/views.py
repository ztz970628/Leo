from QUser.models import *
import hashlib


def set_password(password):

    """
    获取密码,返回加密的密码
    """
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result


# 校验用户是否存在
def vaild_user(email):
    """
    根据email查询 Quser 表,如果不存在 返回False,如果存在返回user
    """
    try:
        user = Quser.objects.get(email=email)
    except Exception as e:
        return False
    else:
        return user


# 用户注册函数
def add_user(**kwargs):
    """
    将用户信息保存到数据库
    """
    if "email" in kwargs and "username" not in kwargs:
        kwargs["username"] = kwargs["email"]
    user = Quser.objects.create(**kwargs)
    return user


def unpdate_user(id,**kwargs):
    pass


def delete_user(id):
    pass




# Create your views here.
