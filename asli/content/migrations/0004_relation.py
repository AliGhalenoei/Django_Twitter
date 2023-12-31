# Generated by Django 4.2.1 on 2023-09-23 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0003_alter_commenttwit_sub'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('twit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='twit_save', to='content.twit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='save_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
