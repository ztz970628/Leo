from django.shortcuts import render_to_response


def tea_demo(request):  # product网页的商品展示栏
    tea_img = [
        {'src': 'upload/pic2.jpg', 't_name': '夏日水果茶', 't_sentence': "这杯果香四溢的水果茶，苹果、菠萝、西瓜、青桔、柠檬。来上一杯，让自己的精神能够在茶香中放松。"},
        {'src': 'upload/pic2.jpg', 't_name': '夏日水果茶', 't_sentence': "这杯果香四溢的水果茶，苹果、菠萝、西瓜、青桔、柠檬。来上一杯，让自己的精神能够在茶香中放松。"},
        {'src': 'upload/pic2.jpg', 't_name': '夏日水果茶', 't_sentence': "这杯果香四溢的水果茶，苹果、菠萝、西瓜、青桔、柠檬。来上一杯，让自己的精神能够在茶香中放松。"},
        {'src': 'upload/pic2.jpg', 't_name': '夏日水果茶', 't_sentence': "这杯果香四溢的水果茶，苹果、菠萝、西瓜、青桔、柠檬。来上一杯，让自己的精神能够在茶香中放松。"},
        {'src': 'upload/pic2.jpg', 't_name': '夏日水果茶', 't_sentence': "这杯果香四溢的水果茶，苹果、菠萝、西瓜、青桔、柠檬。来上一杯，让自己的精神能够在茶香中放松。"},
        {'src': 'upload/pic2.jpg', 't_name': '夏日水果茶', 't_sentence': "这杯果香四溢的水果茶，苹果、菠萝、西瓜、青桔、柠檬。来上一杯，让自己的精神能够在茶香中放松。"},
    ]
    return render_to_response('product.html', locals())


def tem_about_demo(request):   # about 网页的 信息
    tem_team_info = [
        {'num': 1, 'src': '../static/upload/about1.jpg', 'name1': '企业文化', 'name2': 'CORPORATE CULTURE', 'sentence': '【黑茶】为区隔一般的茶饮连锁店，客户导向是我们服务的宗旨，要让每一位来店消费者能享受最好的服务与饮品，故在茶叶的选配、温度的控制、冰块与糖量的多与少都用心专研，每一杯都是新鲜手摇的好茶。'},
        {'num': 2, 'src': '../static/upload/about2.jpg', 'name1': '我们的历史', 'name2': 'OUR HISTORY', 'sentence': '公司主要经营泡沫茶饮，黑茶是以招牌“用新鲜茶叶泡制”茶系为主辅，辅以其它新鲜特色饮料，以及现煮研磨咖啡和更为受广大顾客接受认可的奶茶系列等，近100种产品，可依各地域性的风味来挑选，我们一直坚持‘新鲜、自然、无负担’的健康理念调配呈现给每一位顾客一杯美味舒心、健康、高品质的茶饮。我们的装修以黑白为主色调、尽显其简约、时尚风格。'},
        {'num': 3, 'src': '../static/upload/about3.jpg', 'name1': '我们的规模', 'name2': 'OUR SCALE', 'sentence': '在广大顾客大力支持与员工的共同努力之下，黑茶（深圳）公司规模逐渐扩大，目前在深圳拥有门店31家，湖南、广西、上海、广州、东莞均有分店，是深圳外卖饮品的第一品牌。'},
        {'num': 4, 'src': '../static/upload/about4.jpg', 'name1': '品牌的释义', 'name2': 'INTERPRETATION OF BRAND', 'sentence': '是以中国六大茶系之一——黑茶而命名，而我们的招牌黑茶是以产品的独特配方和颜色取名的。'}
    ]
    return render_to_response('about.html', locals())


def tea_contact_demo(request):
    tea_tx = [
        {'class': 'tx', 'ph': '通讯· TelePhone', 'xx': '24小时手机热线：13609623453 张先生', 'tal': '招商热线：0755-82369636'},
        {'class': 'dz', 'ph': '地址· Address', 'xx': '深圳市黑茶餐饮管理有限公司', 'tal': '地址：深圳罗湖区燕南路沃尔玛楼下黑茶店'},
        {'class': 'td', 'ph': '投递· Delivery', 'xx': '传真：0755-82369456', 'tal': 'E-mail:123456@163.com'}
    ]
    return render_to_response('contact.html', locals())


def tea_index_demo(request):
    tea_img1 = [
        {'src': "../static/upload/banner.jpg"},
        {'src': "../static/upload/banner.jpg"},
        {'src': "../static/upload/banner.jpg"}
    ]
    tea_img2 = [
        {'src': "../static/upload/shouji.jpg"},
        {'src': "../static/upload/shouji.jpg"},
        {'sre': "../static/upload/shouji.jpg"}
    ]
    tea_xx = [
        {'num': 'a', 'wx': ' ', 'name1': '青桔', 'name2': '柠檬', 'xx': '鲜柠檬片的清新与新鲜青桔的酸甜，即解渴又回味无穷的最佳健康饮品'},
        {'num': 'b', 'wx': '冰', 'name1': '摩卡', 'name2': '咖啡', 'xx': '意式浓缩咖啡与巧克力酱结合，顺滑绵密的口感令人无法停止'},
        {'num': 'c', 'wx': ' ', 'name1': '红豆', 'name2': '椰露', 'xx': '特调冰凉的椰奶中加入颗粒饱满的蜜豆，为您奉献一杯经典的海岛椰露'},
        {'num': 'd', 'wx': ' ', 'name1': '招牌', 'name2': '黑茶', 'xx': '口感清新甘甜，又具传统黑茶的醇和口感，是一款具有独特的台湾风味茶饮'},
    ]

    tea_img3 = [
        {'src': '../static/images/pic3.png'},
        {'src': '../static/images/pic4.png'},
        {'src': '../static/images/pic5.png'},
        {'src': '../static/images/pic6.png'}
    ]
    tea_XX = [
        {'num': 'one', 'name': '夏日<em>水果茶</em>', 'src': '../static/images/pic7.png', 'str': '''这杯果香四溢的水果茶，苹果，菠萝，西瓜，青桔，</p>
                    <p>柠檬。来上一杯，让自己的精神</p>
                    <p>能够在茶香中放松。'''},
        {'num': 'two', 'name': '玛丽<em>苏</em>', 'src': '../static/images/pic7.png', 'str': '''采用产自印度红茶作为基底，再添加从法国</p>
                    <p>进口的黑露田，调制出口感清新甘甜，</p>
                    <p>又具传统黑茶的醇和口感'''},
        {'num': 'three', 'name': '黑<em>茶</em>', 'src': '../static/images/pic7.png', 'str': '''采用产自印度红茶作为基底，再添加从法国</p>
                    <p>进口的黑露田，调制出口感清新甘甜，</p>
                    <p>又具传统黑茶的醇和口感'''},
        {'num': 'four', 'name': '青桔<em>柠檬</em>', 'src': '../static/images/pic7.png', 'str': '''青桔与柠檬的碰撞！</p>
                    <p>酸甜滋味加上茶香，全新体验刺激你的味蕾</p>
                    <p>果香清甜，点缀你的夏天'''},
    ]
    tea_img4 = [
        {'name': 'dm_ma', 'src': '../static/upload/pic5.png'},
        {'name': 'dm_mb', 'src': '../static/upload/pic5.png'},
        {'name': 'dm_mc', 'src': '../static/upload/pic5.png'},
        {'name': 'dm_md', 'src': '../static/upload/pic5.png'}
    ]
    return render_to_response('index.html', locals())


def tea_jstore_demo(request):
    tea_DZ = [
        {'name': '燕南店', 'time': '08:00-00:00', 'dz': '广东省深圳市福田区燕南路88号A-9号铺', 'tal': '0755-88391665'},
        {'name': '燕南店', 'time': '08:00-00:00', 'dz': '广东省深圳市福田区燕南路88号A-9号铺', 'tal': '0755-88391665'},
        {'name': '燕南店', 'time': '08:00-00:00', 'dz': '广东省深圳市福田区燕南路88号A-9号铺', 'tal': '0755-88391665'},
        {'name': '燕南店', 'time': '08:00-00:00', 'dz': '广东省深圳市福田区燕南路88号A-9号铺', 'tal': '0755-88391665'},
        {'name': '燕南店', 'time': '08:00-00:00', 'dz': '广东省深圳市福田区燕南路88号A-9号铺', 'tal': '0755-88391665'},
        {'name': '燕南店', 'time': '08:00-00:00', 'dz': '广东省深圳市福田区燕南路88号A-9号铺', 'tal': '0755-88391665'},

    ]
    return  render_to_response('jstore.html', locals())


def tea_news_demo(request):
    tea_xx = [
        {'name': '黑茶7周年加盟优惠活动', 'xx': '黑茶7周年加盟代理优惠活动从7月20日正式启动，针对部分区域和城市，我们现推出零加盟费的方式和您一起成长，共同发展，详情请致电13609623453张先生！', 'time': '2015-07-14'},
        {'name': '黑茶7周年加盟优惠活动', 'xx': '黑茶7周年加盟代理优惠活动从7月20日正式启动，针对部分区域和城市，我们现推出零加盟费的方式和您一起成长，共同发展，详情请致电13609623453张先生！', 'time': '2015-07-14'},
        {'name': '黑茶7周年加盟优惠活动', 'xx': '黑茶7周年加盟代理优惠活动从7月20日正式启动，针对部分区域和城市，我们现推出零加盟费的方式和您一起成长，共同发展，详情请致电13609623453张先生！', 'time': '2015-07-14'}
    ]
    return render_to_response('news.html', locals())
