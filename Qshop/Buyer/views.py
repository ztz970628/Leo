from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from Shop.models import *
from QUser.views import *
from Buyer.models import *
import time


def index(request):
    # 查询所有类型
    type_list = GoodsType.objects.all()
    print(type_list)
    # 查询单个类型
    # type_data = GoodsType.objects.get(id=1)
    # 查询对应类型的所有商品
    # type_data.goods_set.all()
    # 查询每个类型对应的商品
    # for t in type_list:
    #     goods_list = t.goods_set.all()
    # 查询每个类型的对应的4个商品
    # for t in type_list:
    #     goods_list = t.goods_set.all()[:4]
    # result = [{t.name: t.goods_set.all(), 'pic': t.picture} for t in type_list]
    return render(request, 'buyer/index.html', locals())


def goods_list(request, id):
    good_list = Goods.objects.all()
    if id:
        good_type = GoodsType.objects.get(id=int(id))
        good_list = good_type.goods_set.filter(statue=1)
    return render(request, 'buyer/list.html', locals())


def good_data(request, id):
    one_good = Goods.objects.filter(id=id)[0]
    type_list = GoodsType.objects.filter(id=one_good.goods_type_id)[0]
    return render(request, 'buyer/good_data.html', locals())


def login_valid(fun):
    def inner(request, *args, **kwargs):
        referer = request.GET.get('referer')
        cookie_user = request.COOKIES.get('email')
        session_user = request.session.get('email')
        if cookie_user and session_user and cookie_user == session_user:
            return fun(request, *args, **kwargs)
        else:
            login_url = '/Buyer/login/'
            if referer:
                login_url = '/Buyer/login/?referer=%s' % referer
            return HttpResponseRedirect(login_url)
    return inner


@login_valid
def cart(request):
    email = request.COOKIES.get("email")  # 获取用户邮箱
    goods_list = BuyCar.objects.filter(car_user=email)  # 获取用户邮箱对应的购物车数据
    count = len(goods_list)  # 购物车商品的数量
    money = 0
    for x in goods_list:
        money += x.goods_price
    if request.method == "POST":  # 为了接收提交订单
        # 对订单的处理
        data = request.POST
        post_data = []
        # 过滤所有选择的商品的id和购买数量
        for key in data:
            if key.startswith("check"):
                id = key.split("_")[1]
                num = "number_%s" % id
                number = data[num]
                post_data.append((id, number))
        # 保存订单主表
        p_order = Pay_order()
        p_order.order_id = str(time.time()).replace(".", "")
        p_order.order_number = len(post_data)
        p_order.order_user = Quser.objects.get(email=request.COOKIES.get("email"))
        p_order.save()  # 这里没有保存总价

        order_total = 0  # 总价计算
        order_number = 0
        # 循环保存当前订单对应的订单详情
        for id, number in post_data:
            number = int(number)
            goods = Goods.objects.get(id=int(id))
            o_info = Order_info()
            o_info.order_id = p_order
            o_info.goods_name = goods.name
            o_info.goods_number = number
            o_info.goods_price = goods.price
            o_info.goods_total = number * goods.price
            o_info.goods_picture = goods.picture.url
            o_info.order_store = goods.goods_store_id
            o_info.save()
            order_total += o_info.goods_total
        p_order.order_total = order_total  # 保存当前订单的总价
        p_order.save()
        return HttpResponseRedirect("/Buyer/place_order/?order_id=%s" % p_order.order_id)
    return render(request, "buyer/cart.html", locals())


def login(request):
    # 记录登录请求是从哪里到的登录页面
    # referer = request.GET.get('referer')
    if request.GET.get('referer'):
        referer = request.GET.get('referer')
    else:
        referer = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pwd")
        # 判断用户是否存在
        # 如果存在
        user = vaild_user(email)
        if user:
            # 判断密码是否正确
            db_password = user.password
            request_password = set_password(password)
            if db_password == request_password:
                refer = request.POST.get('referer')
                if refer!='None':
                    response = HttpResponseRedirect(refer)
                else:
                    response = HttpResponseRedirect('/')

                response.set_cookie("email", user.email)
                response.set_cookie("user_id", user.id)
                request.session["email"] = user.email
                return response
            else:
                error = "密码错误"
        else:
            error = "用户不存在"
    return render(request, "buyer/login.html", locals())


def logout(request):
    response = HttpResponseRedirect("/Buyer/login/")
    response.delete_cookie('email')
    return response


def pay_result(request):
    data = request.GET
    return render(request,locals())


def add_car(request):
    result = {'state': "error", 'data': ""}
    if request.method == 'POST':
        user = request.COOKIES.get('email')
        goods_id = request.POST.get('goods_id')
        number = request.POST.get('number', 1)
        try:
            goods = Goods.objects.get(id=goods_id)
        except Exception as e:
            result['data'] = str(e)
        else:
            car = BuyCar()
            car.car_user = user
            car.goods_name = goods.name
            car.goods_picture = goods.picture
            car.goods_price = goods.price
            car.goods_number = number
            car.goods_total = int(number) * goods.price
            car.goods_store = goods.goods_store_id
            car.goods_id = goods.id
            car.save()
            result["state"] = "success"
            result["data"] = "加入购物车成功"
    return JsonResponse(result)


def place_order(request):
    return render(request, 'buyer/place_order.html')
# Create your views here.
