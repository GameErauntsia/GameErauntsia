# import json
# import simplejson
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.hashers import make_password
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
#
# from gamerauntsia.app.authentication.models import *
# from functools import wraps
# from django.contrib.auth import authenticate, login
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
# from django.views.decorators.csrf import csrf_exempt
#
#
# @csrf_exempt
# def register(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         user = GamerUser()
#         user.username = data['username']
#         user.password = make_password(data['password'])
#         user.first_name = data['first_name']
#         user.save()
#         token = Token.objects.create(user=user)
#         return json_response({
#             'token': token.token,
#             'username': user.username,
#         })
#
#
# @csrf_exempt
# def userLogin(request):
#     data = {}
#     if request.method == "GET":
#         pass
#     if request.method == "POST":
#         data = json.loads(request.body)
#         uname = data['username']
#         password = data['password']
#         user = authenticate(username=uname, password=password)
#         if user is not None:
#             login(request, user)
#         if user.is_active:
#             token, created = Token.objects.get_or_create(user=user)
#             return json_response({
#                 'token': token.token,
#                 'username': user.username
#             })
#         else:
#             return json_response({
#                 'error': 'Invalid User'
#             }, status=400)
#     else:
#         data = {
#             'message': 'Invalid User Credentials'
#         }
#     data = {
#         'message': 'Invalid'
#     }
#     return HttpResponse(json.dumps(data))
#
#
# def token_required(func):
#     def inner(request, *args, **kwargs):
#         if request.method == 'OPTIONS':
#             return func(request, *args, **kwargs)
#         auth_header = request.META.get('HTTP_AUTHORIZATION', None)
#         if auth_header is not None:
#             tokens = auth_header.split(' ')
#             if len(tokens) == 2 and tokens[0] == 'Token':
#                 token = tokens[1]
#                 try:
#                     request.token = Token.objects.get(token=token)
#                     return func(request, *args, **kwargs)
#                 except Token.DoesNotExist:
#                     return json_response({
#                         'error': 'Token not found'
#                     }, status=401)
#             return json_response({
#                 'error': 'Invalid Header'
#             }, status=401)
#
#     return inner
#
#
# @csrf_exempt
# @token_required
# def userLogout(request):
#     if request.method == 'POST':
#         request.token.delete()
#         return json_response({
#             'status': 'success'
#         })
#     elif request.method == 'OPTIONS':
#         return json_response({})
#     else:
#         return json_response({
#             'error': 'Invalid Method'
#         }, status=405)
#
#
# def json_response(value, **kwargs):
#     kwargs.setdefault('content_type', 'text/javascript; charset=UTF-8')
#     return HttpResponse(simplejson.dumps(value), **kwargs)
