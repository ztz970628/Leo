from django.shortcuts import render_to_response
from django.http import HttpResponse


def func(request):
    f_list = [
        {'img':'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1571133536571&di=6f2c47bf7f4e73ab94097ca460cc2560&imgtype=0&src=http%3A%2F%2Fimg1.cache.netease.com%2Fcatchpic%2F6%2F6A%2F6A10082CA927C56197E7D99250B87437.jpg','name': '李一', 'sex': '男'},
        {'img':'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1571728265&di=b3ca1d710742e8ea4d88c9543d6614e7&imgtype=jpg&er=1&src=http%3A%2F%2Fi1.sinaimg.cn%2Fedu%2F2012%2F0717%2FU3834P42DT20120717152850.jpg','name': '李二', 'sex': '男'},
        # {'name': '李三', 'sex': '男'},
        # {'name': '李四', 'sex': '男'},
        # {'name': '李五', 'sex': '男'},
        # {'name': '李六', 'sex': '女'},
    ]
    return render_to_response('demo_html.html', locals())



