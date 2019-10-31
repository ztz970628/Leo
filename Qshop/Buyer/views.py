from django.shortcuts import render
from Shop.models import *


def index(request):
    # 查询所有类型
    type_list = GoodsType.objects.all()
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

    good_list = Goods.objects.filter(goods_type_id=id)
    type_list = GoodsType.objects.filter(id=id)[0]
    return render(request, 'buyer/list.html', locals())


def good_data(request, id):
    one_good = Goods.objects.filter(id=id)[0]
    type_list = GoodsType.objects.filter(id=one_good.goods_type_id)[0]
    return render(request, 'buyer/good_data.html', locals())



# Create your views here.
