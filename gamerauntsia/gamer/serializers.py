from rest_framework import serializers
from gamerauntsia.gamer.models import GamerUser,JokuPlataforma

class JokuPlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = JokuPlataforma
        depth=1
        fields = ('plataforma', 'nick', 'user')

class GameUserSerializer(serializers.ModelSerializer):
    plat=JokuPlataformaSerializer

    class Meta:
        model = GamerUser
        depth=1
        exclude = ('password','is_superuser','phone','usertype','added_source','is_active',)
#         fields = ('plat',)
#
# class GameUserSerializer(serializers.Serializer):
# 	pk = serializers.IntegerField(read_only=True)
#