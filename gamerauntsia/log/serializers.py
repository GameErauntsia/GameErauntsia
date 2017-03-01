from rest_framework import serializers
from gamerauntsia.log.models import Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        depth = 2

# fields = ('id', 'tituloa', 'deskripzioa', 'mota', 'fetxa', 'user','berria', 'gameplaya',
#                 'post', 'forum')
