from django.http import HttpResponse
import time


def index(request):
    return HttpResponse('hello word')


def ages_num(request, month, day):
    t1 = time.mktime((2019, int(month), int(day), 0, 0, 0, 0, 0, 0))
    t2 = time.localtime(t1).tm_yday
    set1 = '您的生日是 %s 月 %s 日 今年的第 %s 天'% (month, day, t2)
    return HttpResponse(set1)



# def func(request):
#     a = """
#     <html>
#     <head>
#
#     </head>
#     <body>
#         <form action="" method="get">
#             <select name="address">
#                 <option value="0">请选择月份</option>
#                 <option value="1">1</option>
#                 <option value="2">2</option>
#                 <option value="3">3</option>
#                 <option value="4">4</option>
#                 <option value="5">5</option>
#                 <option value="6">6</option>
#                 <option value="7">7</option>
#                 <option value="8">8</option>
#                 <option value="9">9</option>
#                 <option value="10">10</option>
#                 <option value="11">11</option>
#                 <option value="12">12</option>
#         </select>
#         <br>
#         <select name="address">
#                 <option value="0">请选择月份</option>
#                 <option value="1">1</option>
#                 <option value="2">2</option>
#                 <option value="3">3</option>
#                 <option value="4">4</option>
#                 <option value="5">5</option>
#                 <option value="6">6</option>
#                 <option value="7">7</option>
#                 <option value="8">8</option>
#                 <option value="9">9</option>
#                 <option value="10">10</option>
#                 <option value="11">11</option>
#                 <option value="12">12</option>
#                 <option value="13">13</option>
#                 <option value="14">14</option>
#                 <option value="15">15</option>
#                 <option value="16">16</option>
#                 <option value="17">17</option>
#                 <option value="18">18</option>
#                 <option value="19">19</option>
#                 <option value="20">20</option>
#                 <option value="21">21</option>
#                 <option value="22">22</option>
#                 <option value="23">23</option>
#                 <option value="24">24</option>
#                 <option value="25">25</option>
#                 <option value="26">26</option>
#                 <option value="27">27</option>
#                 <option value="28">28</option>
#                 <option value="29">29</option>
#                 <option value="30">30</option>
#                 <option value="31">31</option>
#         </select>
#         <br>
#             <input type="submit" value="提交按钮">
#         </form>
#     </body>
#     </html>
#
#
#     """
#     return HttpResponse(a)



