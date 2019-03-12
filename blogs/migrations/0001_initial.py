# Generated by Django 2.1.7 on 2019-03-11 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('title', models.CharField(max_length=255, verbose_name='Blog title')),
                ('subscribers', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name="Blog's subscribers")),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='blog_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User blog',
                'verbose_name_plural': 'User blogs',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('title', models.CharField(max_length=255, verbose_name='Post title')),
                ('text', models.TextField()),
                ('blog', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blogs.Blog')),
            ],
            options={
                'verbose_name': 'Blog post',
                'verbose_name_plural': 'Blog posts',
                'ordering': ('-updated',),
            },
        ),
        migrations.CreateModel(
            name='ReadMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('is_marked', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='read_marks', to='blogs.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='read_marks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post read mark',
                'verbose_name_plural': 'Post read marks',
                'ordering': ('-updated',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='readmark',
            unique_together={('user', 'post')},
        ),
    ]
