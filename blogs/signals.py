from django.dispatch import receiver
from django.db.models.signals import post_save
from blogs.models import Post
from django.db.models import Q
from django.contrib.sites.models import Site
from django.core.mail import send_mail


@receiver(post_save, sender=Post)
def notify(instance, created, *args, **kwargs):
    if created:
        user = instance.blog.user
        emails_to_send = instance.blog.subscribers.exclude(
            Q(email__isnull=True) | Q(id=user.id)
        ).values_list('email', flat=True)

        url = '{}{}'.format(Site.objects.get_current(), instance.get_absolute_url)
        sbg = 'Simple blog. New post'
        text = 'You have new post. Click to link:  ' + url

        send_mail(sbg, text, 'simple_blog_test_app@gmail.com', emails_to_send)

