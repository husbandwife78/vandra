from django.core import serializers
from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Post, PostPoint, Traveler


class PostListView(ListView):
    model = Post
    template_name = 'main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        coordinates = list(Post.objects.values('slug', 'postLatitude', 'postLongitude'))
        context['post_coordinates'] = coordinates
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'second_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # zoom_coordinates = list(Post.objects.values('slug', 'postLatitude', 'postLongitude'))
        post_points_info = list(PostPoint.objects.values('name', 'latitude',
                                                         'longitude', 'image',
                                                         'post_name'))
        # post_points_info = post_points_info.extend(post_points_info)
        context['post_points'] = post_points_info
        return context


class FriendsListView(ListView):
    model = Traveler
    template_name = 'friends_page.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     coordinates = list(Post.objects.values('slug', 'postLatitude', 'postLongitude'))
    #     context['post_coordinates'] = coordinates
    #     return context
