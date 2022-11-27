# -*- coding: gbk -*-
import json
import os.path
from django.core.exceptions import *
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from secondhand_book.models import *
from django.core.mail import send_mail
# Create your views here.


def index(request):
    return redirect('../homepage/')


def login(request):
    if request.method == 'GET':
        message = None
        if request.session.get('message'):
            message = request.session.get('message')
            request.session['message'] = None
        return render(request, 'login.html', {'message': message})
    if request.method == 'POST':
        ID = request.POST.get("user")
        pwd = str(request.POST.get('pwd'))
        try:
            user = UserInfo.objects.get(Email=ID)
            if pwd == user.password:
                request.session['is_login'] = True
                request.session['ID'] = user.UserID
                request.session.set_expiry(0)
                response = redirect('../homepage/')
                response.set_cookie('ID', ID)
                message_text = '你正在登录校园二手书交易平台，我们向你发送这个邮件进行验证以保证是你本人登录，此上'
                send_mail(subject='你好', message=message_text, from_email='765019392@qq.com',
                          recipient_list=['765019392@qq.com'], fail_silently=False)
                return response
            else:
                return render(request, 'login.html', {'message': '用户名或密码错误'})
        except Exception as e:
            print(e)


def homepage(request, keyword=''):
    print(request.session['ID'])
    if not request.session.get('is_login'):
        request.session['message'] = '登录信息已失效，请重新登入'
        return redirect('../login/')
    if request.method == 'GET':
        goods_list = Goods.objects.filter(
            models.Q(Commodity_Name__icontains=keyword)).values(
            'Img',
            'Commodity_Name',
            'Price',
            'Commodity_ID')
        if not goods_list.exists():
            print("nothing")
            return render(request, 'index_test.html', {'errmsg': '无查询结果'})

        response = render(request, 'index_test.html', {'goods_list': goods_list})
        return response


def personal_info(request):
    if not request.session.get('is_login'):
        request.session['message'] = '登录信息已失效，请重新登入'
        return redirect('../login/')

    # 在判断完登录信息后，我需要获取这个人的信息
    ID = request.session['ID']
    user = UserInfo.objects.get(UserID=ID)

    # 如果这是POST方法
    if request.method == 'POST':
        try:
            file_object = request.FILES.get("head")
            print(file_object.name)
            img_name = str(ID) + '.jpg'
            DIR = os.path.join('secondhand_book', 'static', 'head', img_name)
            f = open(DIR, mode='wb')
            f.seek(0)
            f.truncate()
            for chunk in file_object.chunks():
                f.write(chunk)
            f.close()
        except Exception as e:
            my_info = {'Img': user.Img, 'UserName': user.Username}
            return render(request, 'personal_information.html', {'Img': user.Img, 'UserName': user.Username,
                                                                 'errmsg': '你没有提交任何图片！'})

    # 无论post还是get都需要返回来一个网页
    my_info = {'Img': user.Img, 'UserName': user.Username}
    return render(request, 'personal_information.html', my_info)