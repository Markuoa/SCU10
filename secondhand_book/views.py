# -*- coding: gbk -*-
import json
import os.path
import random
from django.core.exceptions import *
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from secondhand_book.models import *
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
            # print(user.Email)
            # print("true:", type(user.password))
            # print("����:", type(pwd))
            if pwd == user.password:
                request.session['is_login'] = True
                request.session['ID'] = user.UserID
                request.session.set_expiry(0)
                response = redirect('../homepage/')
                response.set_cookie('my_cookie_1:', ID)
                return response
            else:
                return render(request, 'login.html', {'message': '�û������������'})
        except Exception as e:
            return render(request, 'login.html', {'message': '�û������������'})


def homepage(request, keyword=''):
    print(request.session['ID'])
    if not request.session.get('is_login'):
        request.session['message'] = '��¼��Ϣ��ʧЧ�������µ���'
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
            return render(request, 'index_test.html', {'errmsg': '�޲�ѯ���'})

        response = render(request, 'index_test.html', {'goods_list': goods_list})
        return response


def personal_info(request):
    if not request.session.get('is_login'):
        request.session['message'] = '��¼��Ϣ��ʧЧ�������µ���'
        return redirect('../login/')

    # ���ж����¼��Ϣ������Ҫ��ȡ����˵���Ϣ
    ID = request.session['ID']
    user = UserInfo.objects.get(UserID=ID)

    # �������POST����
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
                                                                 'errmsg': '��û���ύ�κ�ͼƬ��'})

    # ����post����get����Ҫ������һ����ҳ
    my_info = {'Img': user.Img, 'UserName': user.Username}
    return render(request, 'personal_information.html', my_info)
