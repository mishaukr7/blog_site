from django.views.generic import ListView, CreateView, DetailView, View
from blogs.models import Post, Blog, ReadMark
from blogs.forms import PostForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


class PostFeed(ListView):
    template_name = 'blogs/feed.html'
    context_object_name = 'feeds'
    model = Post
    ordering = ('-updated', )

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(blog__in=user.user_subscribers.all())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['marked'] = ReadMark.objects.filter(user=self.request.user).values_list('post', flat=True)
        return context


class PostListView(ListView):
    template_name = 'blogs/own_posts.html'
    context_object_name = 'posts'
    model = Post
    ordering = ('-updated', )

    def get_queryset(self):
        return Post.objects.filter(blog__user=self.request.user)


class PostCreateView(CreateView):
    form_class = PostForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.blog = self.request.user.blog_user
        obj.save()
        ReadMark.objects.create(
            user=self.request.user,
            post=obj
        )
        return super(PostCreateView, self).form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/post_detail.html'
    context_object_name = 'post'


class ReadMarkView(View):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        read_mark, _ = ReadMark.objects.get_or_create(
            user=request.user,
            post=post,
        )
        return HttpResponseRedirect(reverse('blogs:feed'))
