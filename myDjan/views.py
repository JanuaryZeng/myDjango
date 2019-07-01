import datetime

import os
import simplejson as simplejson
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json

from myDjango.settings import BASE_DIR
from .models import lovertable
from .serializers import lovertableSerializer
from .models import moneychangetable, moneytypetable,notetable,usertable,friendtable
from .serializers import moneychangetableSerializer, moneytypetableSerializer,notetableSerializer,usertableSerializer,friendtableSerializer


# 规定该方法只能通过post、get和delete请求
@api_view(['POST', 'GET', 'DELETE'])
# request就是你的请求
def user_api(request):
    # 如果请求是get
    if request.method == 'GET':

        # 获取user表全部的用户
        users = lovertable.objects.all()

        # 将获取结果序列化，当many=True的时候才允许返回多条数据，不然报错
        serializer = lovertableSerializer(users, many=True)

        # serializer.data是一个字典，status是状态码，2XX是成功返回
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 如果请求是post
    elif request.method == 'POST':

        # request.data也是一个字典，有兴趣可以 print(request.data)
        serializer = lovertableSerializer(data=request.data)

        print(request.data)
        print(serializer.is_valid())

        # 如果数据符合规定，字符长度之类的
        if serializer.is_valid():
            # 保存
            serializer.save()

            # 同上
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # 如果不符合规定
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # 如果是delete请求
    elif request.method == 'DELETE':

        # 删除全部用户
        lovertable.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 同上
@api_view(['GET', 'PUT', 'DELETE'])
# name是参数，这不是我常用的方法，仅仅是和大家说有这样的用法
def another_user_api(request, userid):
    # 同上
    if request.method == 'GET':

        # 获取单个用户，其中name是字段名，username是参数
        # user = User.objects.get(name=username)

        # 由于我在models中没写不允许字段重复，所有get方法当有字段重复时会报错
        # filter就是根据条件查找，first很容易理解，就是第一条数据
        user = lovertable.objects.filter(loverid=userid).first()

        # 将结果序列化，不需要many=True
        serializer = lovertableSerializer(user)

        # 同上
        return Response(serializer.data, status=status.HTTP_200_OK)

    # put一般是修改
    elif request.method == 'PUT':

        # 同上
        user = lovertable.objects.filter(loverid=userid).first()

        # 同上，request.data是传入的要修改的新数据
        # 先把要修改的那条数据从数据库中获取，然后修改数据，保存
        serializer = lovertableSerializer(user, data=request.data)

        # 同样要检查数据合法性
        if serializer.is_valid():
            # 合法
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

            # 不合法
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        # 同上
        user = lovertable.objects.filter(name=userid).first()

        # 删除
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def android_user_api(request):
    if request.method == 'POST':
        _data = dict(request.data)
        # 之前说过request.data是一个字典，可以利用这个
        # fields = ('loverid', 'lovernumber','loverpassword','loverdate','moneyout','moneyin')

        if _data['table'][0] == 'lovertable':
            if _data['method'][0] == '_GET':
                user = lovertable.objects.get(loverid=_data['loverid'][0], loverpassword=_data['loverpassword'][0])
                serializer = lovertableSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif _data['method'][0] == '_POST':
                # request.data 中多余的数据不会保存到数据库中
                serializer = lovertableSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            elif _data['method'][0] == '_PUT':
                user = lovertable.objects.get(loverid=_data['loverid'][0])
                serializer = lovertableSerializer(user, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            elif _data['method'][0] == '_DELETE':
                lovertable.objects.get(loverid=_data['loverid'][0]).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            elif _data['method'][0] == '_Money':
                if _data['Mate'][0] == '_GET':
                    user = lovertable.objects.get(loverid=_data['loverid'][0])
                    serializer = lovertableSerializer(user)
                    return Response(serializer.data, status=status.HTTP_200_OK)

        # moneychangetable
        elif _data['table'][0] == 'moneychangetable':

            if _data['method'][0] == '_GET':
                try:
                    mon_change_obj = moneychangetable.objects.filter(loverid=_data['loverid'][0])
                except moneychangetable.DoesNotExist:
                    return Response('参数不存在')
                ser = moneychangetableSerializer(instance=mon_change_obj, many=True)
                return Response(ser.data, status=status.HTTP_200_OK)

            elif _data['method'][0] == '_POST':
                # request.data 中多余的数据不会保存到数据库中
                serializer = moneychangetableSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            elif _data['method'][0] == '_PUT':
                user = moneychangetable.objects.get(moneychangeid=_data['moneychangeid'][0])
                serializer = moneychangetableSerializer(user, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            elif _data['method'][0] == '_DELETE':
                moneychangetable.objects.get(moneychangeid=_data['moneychangeid'][0],loverid=_data['loverid'][0]).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

        elif _data['table'][0] == 'moneytypetable':

            if _data['method'][0] == '_GET':
                try:
                    mon_change_obj = moneytypetable.objects.filter()
                except moneytypetable.DoesNotExist:
                    return Response('参数不存在')
                ser = moneytypetableSerializer(instance=mon_change_obj, many=True)
                return Response(ser.data, status=status.HTTP_200_OK)
        elif _data['table'][0] == 'notetable':
            if _data['method'][0] == '_GET':
                try:
                    mon_change_obj = notetable.objects.filter(loverid=_data['loverid'][0])
                except notetable.DoesNotExist:
                    return Response('参数不存在')
                ser = notetableSerializer(instance=mon_change_obj, many=True)
                return Response(ser.data, status=status.HTTP_200_OK)
            elif _data['method'][0] == '_POST':
                # request.data 中多余的数据不会保存到数据库中
                serializer = notetableSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            elif _data['method'][0] == '_PUT':
                user = notetable.objects.get(noteid=_data['noteid'][0])
                serializer = notetableSerializer(user, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            elif _data['method'][0] == '_DELETE':
                notetable.objects.get(noteid=_data['noteid'][0]).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        elif _data['table'][0] == 'usertable':
            if _data['method'][0] == '_GET':
                try:
                    mon_change_obj = usertable.objects.filter(loverid=_data['loverid'][0])
                except notetable.DoesNotExist:
                    return Response('参数不存在')
                ser = usertableSerializer(instance=mon_change_obj, many=True)
                return Response(ser.data, status=status.HTTP_200_OK)
        elif _data['table'][0] == 'friendtable':
            if _data['method'][0] == '_GET':
                try:
                    mon_change_obj = friendtable.objects.filter(loverid=_data['loverid'][0])
                except notetable.DoesNotExist:
                    return Response('参数不存在')
                ser = friendtableSerializer(instance=mon_change_obj, many=True)
                return Response(ser.data, status=status.HTTP_200_OK)
            elif _data['method'][0] == '_DELETE':
                friendtable.objects.get(friendid=_data['friendid'][0]).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

        # if _data['method'][0] == '_GET':
        #     user = lovertable.objects.get(loverid=_data['loverid'][0])
        #     serializer = lovertableSerializer(user)
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # elif _data['method'][0] == '_POST':
        #     # request.data 中多余的数据不会保存到数据库中
        #     serializer = lovertableSerializer(data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        # elif _data['method'][0] == '_PUT':
        #     user = lovertable.objects.get(loverid=_data['loverid'][0])
        #     serializer = lovertableSerializer(user, data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        # elif _data['method'][0] == '_DELETE':
        #     lovertable.objects.get(loverid=_data['loverid'][0]).delete()
        #     return Response(status=status.HTTP_204_NO_CONTENT)


def uploadImages(request):
    print(request)
    if True:

        url_sets = list()

        len = int(request.POST.get('len'))

        loverid = request.POST.get('loverid')
        usergender = request.POST.get('usergender')
        frienddate = request.POST.get('frienddate')
        friendtext = request.POST.get('friendtext')

        _data = dict()
        _data.update({'loverid':loverid})
        _data.update({'usergender':usergender})
        _data.update({'frienddate':frienddate})
        _data.update({'friendtext':friendtext})

        # print("*-*-*-*-*-*-*-/*-/*-/*-/-*/*-",friendtext)

        source1 = ['sourcefiles0','sourcefiles1']
        source2 = ['sourcefiles2','sourcefiles3']
        source3 = ['sourcefiles4','sourcefiles5']
        source4 = ['sourcefiles6','sourcefiles7','sourcefiles8']

        url_sets.clear()
        for i in source1:
            if len <= 0:
                break
            len = len - 1
            sourcefiles = request.FILES[i]
            if sourcefiles.content_type == 'application/octet-stream' or sourcefiles.content_type == 'image/jpeg' or sourcefiles.content_type == 'application/x-jpg' or sourcefiles.content_type == 'image/png' or sourcefiles.content_type == 'application/x-png' or sourcefiles.content_type == 'text/plain':
                file_path, path = save_uploaded_file(sourcefiles)
                url_sets.append(path)
            pathur = '去'.join(url_sets)
            print("------********-----", pathur)
            _data.update({'friendphotos1': pathur})

        url_sets.clear()
        for i in source2:
            if len <= 0:
                break
            len = len - 1

            sourcefiles = request.FILES[i]
            if sourcefiles.content_type == 'application/octet-stream' or sourcefiles.content_type == 'image/jpeg' or sourcefiles.content_type == 'application/x-jpg' or sourcefiles.content_type == 'image/png' or sourcefiles.content_type == 'application/x-png' or sourcefiles.content_type == 'text/plain':
                file_path, path = save_uploaded_file(sourcefiles)
                url_sets.append(path)
            pathur = '去'.join(url_sets)
            print("------********-----", pathur)
            _data.update({'friendphotos2': pathur})

        url_sets.clear()
        for i in source3:
            if len <= 0:
                break
            len = len - 1

            sourcefiles = request.FILES[i]
            if sourcefiles.content_type == 'application/octet-stream' or sourcefiles.content_type == 'image/jpeg' or sourcefiles.content_type == 'application/x-jpg' or sourcefiles.content_type == 'image/png' or sourcefiles.content_type == 'application/x-png' or sourcefiles.content_type == 'text/plain':
                file_path, path = save_uploaded_file(sourcefiles)
                url_sets.append(path)
            pathur = '去'.join(url_sets)
            print("------********-----", pathur)
            _data.update({'friendphotos3': pathur})

        url_sets.clear()
        for i in source4:
            if len <= 0:
                break
            len = len - 1

            sourcefiles = request.FILES[i]
            if sourcefiles.content_type == 'application/octet-stream' or sourcefiles.content_type == 'image/jpeg' or sourcefiles.content_type == 'application/x-jpg' or sourcefiles.content_type == 'image/png' or sourcefiles.content_type == 'application/x-png' or sourcefiles.content_type == 'text/plain':
                file_path, path = save_uploaded_file(sourcefiles)
                url_sets.append(path)
            pathur = '去'.join(url_sets)
            print("------********-----", pathur)
            _data.update({'friendphotos4': pathur})


        friend = friendtableSerializer(data=_data)
        a = {'data': _data}

        if friend.is_valid():
            friend.save()
            return HttpResponse(a, 'application/javascript')
            # 取出验证失败的信息,方便定位问题,给用用户提示
        else:
            ErrorDict = friend.errors

            Error_Str = json.dumps(ErrorDict)

            Error_Dict = json.loads(Error_Str)
            print(Error_Dict)
        return HttpResponse(a, 'application/javascript')

def save_uploaded_file(sourcefiles):#将图片储存下来
    filename = sourcefiles.name
    filePath = os.path.join(BASE_DIR, 'media').replace('\\', '/') + '/'+ filename
    path = os.path.join("http://10.0.116.45:8000/media/",filename)
    destination = open(filePath, 'wb+')
    try:
        for chunk in sourcefiles.chunks():
            destination.write(chunk)
    except Exception as e:
        print ("save_uploaded_file----%s : %s" % (Exception, e))
    finally:
        destination.close()
    return filePath,path

def upLoadIcon(request):
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",request)

    userid = request.POST.get('userid')
    usergender = request.POST.get('usergender')
    username = request.POST.get('username')
    userborn = request.POST.get('userborn')


    _data = dict()
    _data.update({'userid': userid})
    _data.update({'usergender': usergender})
    _data.update({'username': username})
    _data.update({'userborn': userborn})
    print("**********----------------************")

    sourcefiles = request.FILES['icon']
    print("**********----------------************")

    if sourcefiles.content_type == 'application/octet-stream' or sourcefiles.content_type == 'image/jpeg' or sourcefiles.content_type == 'application/x-jpg' or sourcefiles.content_type == 'image/png' or sourcefiles.content_type == 'application/x-png' or sourcefiles.content_type == 'text/plain':
        file_path, path = save_uploaded_file(sourcefiles)
        _data.update('usericon',path)
    a = {'data',_data}

    user = usertableSerializer(data = _data)
    if user.is_valid():
        user.save()
        return HttpResponse(a, 'application/javascript')
    else:
        ErrorDict = user.errors

        Error_Str = json.dumps(ErrorDict)

        Error_Dict = json.loads(Error_Str)
        print(Error_Dict)
    return HttpResponse(a, 'application/javascript')