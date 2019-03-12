from django.db import models
from users.models import User
from django.urls import reverse


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated date')

    class Meta:
        abstract = True


class Blog(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='blog_user')
    subscribers = models.ManyToManyField(
        User, blank=True,
        verbose_name='Blog\'s subscribers',
        related_name='user_subscribers'
    )
    title = models.CharField(max_length=255, verbose_name='Blog title')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'User blog'
        verbose_name_plural = 'User blogs'
        ordering = ('-created', )


class Post(TimeStampedModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255, verbose_name='Post title')
    text = models.TextField()

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Blog post'
        verbose_name_plural = 'Blog posts'
        ordering = ('-updated', )

    def get_absolute_url(self):
        return reverse('blogs:post_detail', args=(self.pk, ))


class ReadMark(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='read_marks')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='read_marks')
    is_marked = models.BooleanField(default=True)

    def __str__(self):
        return '{}-{}'.format(self.user.username, self.post.title)

    class Meta:
        verbose_name = 'Post read mark'
        verbose_name_plural = 'Post read marks'
        unique_together = ('user', 'post', )
        ordering = ('-updated', )


