from rest_framework import serializers
from gamerauntsia.berriak.models import Berria
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class BerriaSerializer(serializers.ModelSerializer):
    irudia = serializers.ReadOnlyField(source='irudia.get_blog_url')
    irudia2 = serializers.ReadOnlyField(source='irudia.image.url')

    class Meta:
        model = Berria
        depth = 1

# fields = ('id', 'izena', 'desk', 'arauak', 'saria', 'irudia','irudia2', 'mota',
#                 'modalitatea', 'status','pub_date', 'insk_date', 'jokalariak')
