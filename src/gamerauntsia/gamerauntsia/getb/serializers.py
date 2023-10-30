from rest_framework import serializers
from gamerauntsia.getb.models import Atala


class GetbSerializer(serializers.ModelSerializer):
    # 	irudia = serializers.ReadOnlyField(source='irudia.get_blog_url')
    # 	irudia2 = serializers.ReadOnlyField(source='irudia.image.url')

    class Meta:
        model = Atala
        depth = 1


# fields = ('izenburua','slug','desk', 'irudia2',)
