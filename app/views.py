from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.utils import IntegrityError
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render_to_response

from .models import *

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, parser_classes, permission_classes
from django_ajax.decorators import ajax
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render_to_response('course-hunter.html')

# @ajax
@api_view(['GET'])
# @parser_classes((JSONParser,))
def hello(request):
    return JsonResponse({"1":1, "2":2}, safe=False)
    # return {'result': 3}
    # return render_to_response('test.html')

## ------------------------------- Authentication Related --------------------------
# # @csrf_exempt
@api_view(['POST'])
def app_login(request):
    email = request.data.get('email')
    passwd = request.data.get('password')

    # print (email)
    # user = User.objects.get(username=email)
    # print (user.password)
    # print (email)
    # print (user.username)
    # print (email == user.username)
    # print (passwd == user.password)
    user = authenticate(username=email, password=passwd)
    if user:
        login(request._request, user)
    else:
        print('failed')
        return Response({"token": ""}, status=status.HTTP_403_FORBIDDEN)
    
    # generate token for client
    print("generate token")
    token, _ = Token.objects.get_or_create(user=user)
    r = JsonResponse({"token": token.key}, status=status.HTTP_202_ACCEPTED)
    r.set_cookie(key="token", value=token.key)
    print(token.key)
    return r

@csrf_exempt
# @csrf_protect 
@api_view(['POST']) 
def app_register(request):

    print('register called')
    email = request.data.get('email')
    passwd = request.data.get('password')
    print(email, passwd)

    try:
        u = User(username=email, password=passwd)
        u.set_password(passwd)
        u.save()
        # return HttpResponse(status = 201)
        return Response(status=status.HTTP_201_CREATED)
    except IntegrityError:
        return Response(status=status.HTTP_409_CONFLICT)

    return HttpResponse(status = 201)

# @csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def app_logout(request):
    logout(request._request)
    request.user.auth_token.delete()
    r = Response() 
    r.delete_cookie('token')
    r.status_code = status.HTTP_200_OK
    return r