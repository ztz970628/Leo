from django.http import HttpResponse
import random  # 导入随机包


def windmill(request):
    str1 = """
        <html>
        <head>
        </head>
        <body>
            <h1 class='c1'><br>%s</br></h1>
        </body>
        </html>
        """
    str2 = ''
    for a in range(1, 10):
        num1 = random.randint(0, 255)
        num2 = random.randint(0, 255)
        num3 = random.randint(0, 255)
        str2 += '<div style="color:rgb(%d,%d,%d)">' % (num1, num2, num3)  # 随机颜色
        for x in range(1, a + 1):
            str2 += (str(x) + '*' + str(a) + '=' + str(a * x) + '  ')
        str2 += '</div>'
    return HttpResponse(str1 % str2)