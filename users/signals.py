from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User
from blogs.models import Blog


@receiver(post_save, sender=User)
def create_blog(instance, created, **kwargs):
    if created:
        Blog.objects.create(
            user=instance,
            title='{}\'s personal blog'.format(instance.username)
        )

