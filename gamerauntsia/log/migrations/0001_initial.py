# Generated by Django 2.2.2 on 2019-06-17 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_forum_app', '0001_initial'),
        ('berriak', '0003_auto_20190617_1316'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gameplaya', '0003_auto_20190617_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloa', models.CharField(blank=True, max_length=100, null=True)),
                ('deskripzioa', models.TextField(blank=True, null=True, verbose_name='Deskripzioa')),
                ('mota', models.CharField(blank=True, max_length=100, null=True)),
                ('fetxa', models.DateTimeField(auto_now_add=True)),
                ('berria', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='log', to='berriak.Berria')),
                ('forum', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='log', to='django_forum_app.Forum')),
                ('gameplaya', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='log', to='gameplaya.GamePlaya')),
                ('post', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='log', to='django_forum_app.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='log', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Log',
            },
        ),
    ]
