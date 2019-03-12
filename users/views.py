from django.views.generic import ListView, View
from users.models import User
from blogs.models import Blog, ReadMark, Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import transaction


class BlogersView(ListView):
    template_name = 'blogs/blogers.html'
    model = User
    context_object_name = 'blogers'

    def get_queryset(self):
        return User.objects.exclude(pk=self.request.user.id)


class SubscribeView(View):
    def post(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=self.kwargs.get('pk'))
        if request.user in blog.subscribers.all():
            with transaction.atomic():
                blog.subscribers.remove(request.user)
                print(blog.posts.all())
                print(ReadMark.objects.filter(
                    user=self.request.user,
                    post__in=blog.posts.all(),
                ))
                ReadMark.objects.filter(
                    user=self.request.user,
                    post__in=blog.posts.all(),
                ).delete()
        else:
            blog.subscribers.add(request.user)
        return HttpResponseRedirect(reverse('users:blogers'))
