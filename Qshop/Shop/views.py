from django.shortcuts import render
from django.http import HttpResponseRedirect
from QUser.views import *
from Shop.models import *
import smtplib
from email.mime.text import MIMEText


def sendMial(content,email):
    from Qshop.settings import MAIL_SENDER,MAIL_PASSWORD,MAIL_SERVER,MAIL_PORT
    content = """
        如果确认是本人修改密码，请点击下放链接进行密码修改
        <a href="%s">点击链接确认</a>
    """ % content
    print(content)
    # 构建邮件格式
    message = MIMEText(content, "html", "utf-8")
    message["To"] = email
    message["From"] = MAIL_SENDER
    message["Subject"] = "密码修改"

    # 发送邮件
    smtp = smtplib.SMTP_SSL(MAIL_SERVER, MAIL_PORT)
    smtp.login(MAIL_SENDER, MAIL_PASSWORD)
    smtp.sendmail(MAIL_SENDER, [email], message.as_string())
    smtp.close()


# 校验登录
def login_valid(func):
    def inner(request, *args, **kwargs):
        cookie_user = request.COOKIES.get('email')
        session_user = request.session.get('email')
        if cookie_user and session_user and cookie_user == session_user:
            user = Quser.objects.get(email=cookie_user)
            identity = user.identity
            if identity >= 1:
                return func(request, *args, **kwargs)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/Shop/login/')
    return inner


def register(request):
    """
    后台卖家注册功能
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        error = ''
        if vaild_user(email):
            error = '当前邮箱注册过'
            # 注册过 提示邮箱注册过

        else:
            # 对密码加密
            password = set_password(password)
            # 添加数据到数据库中
            add_user(email=email, password=password)
            # 跳转到登录
            return HttpResponseRedirect('/Shop/login/')
    return render(request, 'shop/register.html', locals())


def login(request):
    error = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = vaild_user(email)
        if user:
            db_password = user.password
            request_password = set_password(password)
            if db_password == request_password:
                response = HttpResponseRedirect("/Shop/")
                response.set_cookie("email", user.email)
                response.set_cookie("user_id", user.id)
                request.session["email"] = user.email
                return response
            else:
                error = '您输入的密码有错'
        else:
            error = '用户不存在,请注册!'

    return render(request, 'shop/login.html', locals())

"""
后台卖家登录功能
"""


@login_valid
def index(request):
    """
    后台卖家功能
    """
    return render(request, 'shop/index.html')


def logout(request):
    """
    后台卖家退出登录功能
    """
    response = HttpResponseRedirect("/Shop/login/")
    response.delete_cookie("email")
    response.delete_cookie("user_id")
    request.session.clear()
    return response


def forget_password(request):
    """
    后台卖家忘记密码功能
    """
    return render(request, 'shop/forgot-password.html')
# Create your views here.


def reset_password(request):
    """
    重置密码
    1,接收发过来的邮箱,进行校验
    """
    if request.method == 'POST':
        # 判断是否为POST请求
        email = request.POST.get('email')
        # 获取请求的email
        if email and vaild_user(email):  # 判断 email存在和 在数据库中有信息
            hash_code = set_password(email)   # email进行加密
            content = 'http://127.0.0.1:8000/Shop/change_password/?email=%s&token=%s' % (email, hash_code)
            sendMial(content, email)

    return HttpResponseRedirect('/Shop/forget_password/')


def change_password(request):
    """
    当前是否是本人修密码
    """
    if request.method == 'POST':
        email = request.COOKIES.get('email')
        password = request.POST.get('password')

        e = Quser.objects.get(email=email)
        e.password = set_password(password)
        e.save()
        return HttpResponseRedirect('/Shop/login/')
        # 通过get请求获得了修改密码的用户和校验值
    email = request.GET.get("email")
    token = request.GET.get("token")
    # 进行再次校验
    now_token = set_password(email)
    # 当前提交人存在，并且token值正确
    if vaild_user(email) and now_token == token:
        # 返回修改密码页面
        response = render(request, "shop/change_password.html")
        # 设置cookie
        response.set_cookie("email", email)
        return response
    else:
        return HttpResponseRedirect("/Shop/forget_password/")


from django.http import HttpResponse
from CeleryTask.tasks import add  # 导入执行的任务


def get_celery(request):
    x = 1
    y = 2
    add.delay(x, y)  # 调用celery任务使用 启动任务
    # sendMial(content, email)
    # print(add.result)
    return HttpResponse('调用完成')


@login_valid
def profile(request):
    """
    个人中心
    """
    user_email = request.COOKIES.get('email')
    user = Quser.objects.get(email=user_email)
    if request.method == "POST":
        password = request.POST.get('password')
        user.password = set_password(password)
        user.save()
        response = HttpResponseRedirect("/Shop/login/")
        response.delete_cookie("email")
        response.delete_cookie("user_id")
        request.session.clear()
        return HttpResponseRedirect('/Shop/login/')
        # 修改完成删除cookie和session然后重新登录
    return render(request, 'shop/profile.html', {"user": user})


@login_valid
def set_profile(request):
    """
    个人中心
    """
    user_email = request.COOKIES.get('email')
    user = Quser.objects.get(email=user_email)
    if request.method == 'POST':
        post_data = request.POST
        username = post_data.get('username')
        gender = post_data.get("gender")
        age = post_data.get("age")
        phone = post_data.get('phone')
        address = post_data.get('address')
        picture = request.FILES.get('picture')

        user.username = username
        user.gender = gender
        user.age = age
        user.phone = phone
        user.address = address
        if picture:
            user.picture = picture
        user.save()
        return HttpResponseRedirect('/Shop/profile/')
    return render(request, 'shop/set_profile.html', {'user': user})


def list_goods(request):
    goods_list = Goods.objects.all()
    return render(request, 'shop/list_goods.html', locals())


def set_goods(request, id):
    goods = Goods.objects.filter(id=int(id))
    if goods[0].statue == 0:
        goods.update(statue=1)
    else:
        goods.update(statue=0)
    return HttpResponseRedirect('/Shop/vue_list_goods/')


def goods(request, id):
    goods_data = Goods.objects.get(id=id)
    return render(request, 'shop/goods.html', locals())


@login_valid
def add_update_goods(request, id=None):
    if id:
        goods_update = Goods.objects.get(id=id)
    else:
        goods_update = Goods()
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        production = request.POST.get('production').replace('年', '-').replace('月', '-').replace('日', '')
        safe_date = request.POST.get('safe_date')
        picture = request.FILES.get('picture')
        description = request.POST.get('description')

        goods_update.name = name
        goods_update.price = price
        goods_update.number = number
        goods_update.production = production
        goods_update.safe_date = safe_date
        goods_update.picture = picture
        goods_update.description = description
        goods_update.save()
        return HttpResponseRedirect('/Shop/goods/%s' % goods_update.id + '/')
    return render(request, 'shop/add_update_goods.html', locals())


from django.views import View
from django.http import JsonResponse
from django.core.paginator import Paginator
# from Qshop.settings import PAZE_SIZE


class GoodsView(View):
    def get(self, request):
        result = {
            'version': 'v1',
            'code': '200',
            'data': [],
            'page-range': [],
            'referer': ''
        }
        id = request.GET.get('id')
        if id:
            goods_data = Goods.objects.get(id=int(id))
            result['data'].append(
                {'id': goods_data.id,
                    'name': goods_data.name,
                    'price': goods_data.price,
                    'number': goods_data.number,
                    'production': goods_data.production,
                    'safe_data': goods_data.safe_date,
                    'picture': goods_data.picture.url,
                    'description': goods_data.description,
                    'statue': goods_data.statue
                }
            )
        else:
            # 尝试获取页码,如果页码不存在,默认是第一页
            page_number = request.GET.get('page', 1)
            # 尝试获取数据
            keywords = request.GET.get('keywords')
            # 获取所有数据
            all_goods = Goods.objects.all()
            if keywords:  # 如果有值,查询对应值
                all_goods = Goods.objects.filter(name__contains=keywords)
                result['referer'] = '&keywords=%s' % keywords
            # 进行分页
            paginator = Paginator(all_goods, 7)
            # 获取单页数据
            page_data = paginator.page(page_number)
            # 获取页码
            result['page_range'] = list(paginator.page_range)
            goods_data = [{"id": g.id,
                           "name": g.name,
                           "price": g.price,
                           "number": g.number,
                           "production": g.production,
                           "safe_date": g.safe_date,
                           "picture": g.picture.url,
                           "description": g.description,
                           "statue": g.statue} for g in page_data
                ]
            result["data"] = goods_data
        return JsonResponse(result)


def vue_list_goods(request):
    return render(request, 'shop/vue_list_goods.html', locals())

