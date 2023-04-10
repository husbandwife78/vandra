from django.core import serializers
from django.shortcuts import render

from django.views.generic import ListView, DetailView
# from rest_framework.serializers import ModelSerializer
# from rest_framework.viewsets import ModelViewSet

from .models import Post


# class PostSerializer(ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['postLatitude', 'postLongitude']
#
#
# class PostSerializerView(ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostListView(ListView):
    model = Post
    template_name = 'main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_coordinates'] = serializers.serialize('json',
                                                            Post.objects.all(),
                                                            fields=['postLatitude', 'postLongitude'])
        # print(context['post_coordinates'])
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'second_page.html'
