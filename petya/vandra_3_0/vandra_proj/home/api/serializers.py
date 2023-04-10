from rest_framework.serializers import ModelSerializer

from home.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'postLatitude', 'postLongitude']
