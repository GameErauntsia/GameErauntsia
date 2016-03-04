from django.db.models.signals import pre_save, post_save
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

# import models
from gamerauntsia.gamer.models import GamerUser
# import serializers
from app.authentication.serializers import UsersListSerializer, UsersCreateSerializer, UsersUpdateSerializer


class CustomModelViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        serializer_class = self.parser['default']
        if getattr(self, 'action') in self.parser:
            serializer_class = self.parser[getattr(self, 'action')]
        if self.request.user.is_superuser:
            if 'admin_' + getattr(self, 'action') in self.parser:
                serializer_class = self.parser['admin_' + getattr(self, 'action')]
        return serializer_class

    def create(self, request, *args, **kwargs):
        data = request.DATA
        if hasattr(self, 'populate'):
            data = self.populate(request, request.DATA, 'create')
            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                self.object = serializer.save()
                if hasattr(self, 'post_save'):
                    self.post_save(self.object, created=True)
                headers = self.get_success_headers(serializer.data)
                if request.accepted_renderer.format == 'json':
                    return Response({'result': serializer.data, 'lookup_field': self.lookup_field,
                                     'resource_uri': request.path + str(getattr(self.object, self.lookup_field)) + '/'},
                                    status=status.HTTP_201_CREATED, headers=headers)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    data = request.data
    if hasattr(self, 'populate'):
        try:
            data = self.populate(request, request.data, 'update')
        except:
            pass
    serializer = self.get_serializer(instance, data=data, partial=partial)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)
    if hasattr(self, 'post_save'):
        self.post_save(instance, created=False)
    return Response(serializer.data)


@csrf_exempt
def dispatch(self, request, *args, **kwargs):
    """
    `.dispatch()` is pretty much the same as Django's regular dispatch,
    but with extra hooks for startup, finalize, and exception handling.
    """
    self.args = args
    self.kwargs = kwargs
    ###
    ### added in compatibility with lookup field
    if 'lookup' in kwargs:
        kwargs['lookup'] = int(kwargs['lookup'])
    ###
    request = self.initialize_request(request, *args, **kwargs)
    self.request = request
    self.headers = self.default_response_headers  # deprecate?

    try:
        self.initial(request, *args, **kwargs)

        # Get the appropriate handler method
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(),
                              self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed

        response = handler(request, *args, **kwargs)

    except Exception as exc:
        response = self.handle_exception(exc)

    self.response = self.finalize_response(request, response, *args, **kwargs)
    return self.response


parser = {
    'detail': UsersListSerializer,
    'update': UsersUpdateSerializer,
    'default': UsersListSerializer
}

pre_save


def populate(self, request, data, mode):
    return data


post_save


def post_save(self, obj, created):
    pass


class UsersViewSet(CustomModelViewSet):
    queryset = GamerUser.objects.all()
    parser = {
        'detail': UsersListSerializer,
        'create': UsersCreateSerializer,
        'update': UsersUpdateSerializer,
        'default': UsersListSerializer
    }
    lookup_field = "username"
    filter_fields = ('username', 'first_name')

    def filtering(self, params, queryset, user=None):
        if "first_name" in params and params['first_name'] != "":
            queryset = queryset.filter(first_name__icontains=params['first_name'])
        if "username" in params and params['username'] != "":
            queryset = queryset.filter(username=params['username'])
        return queryset

    def create(self, *args, **kwargs):
        return Response({'message': 'Invalid Request'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, *args, **kwargs):
        if self.request.user.username == kwargs['username']:
            return super(UsersViewSet, self).update(*args, **kwargs)
        else:
            return Response({'message':'Youre not Authorized'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, *args, **kwargs):
        return Response({'message':'Invalid Request'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)