# Generated by Django 2.0.9 on 2018-12-30 11:58

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
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweeter_user', models.CharField(blank=True, max_length=300, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('create', models.DateField(blank=True, null=True)),
                ('hour', models.IntegerField(blank=True, null=True)),
                ('locate', models.TextField(blank=True, null=True)),
                ('num_word', models.IntegerField(blank=True, null=True)),
                ('num_letter', models.IntegerField(blank=True, null=True)),
                ('tag', models.TextField(blank=True, default='#Python', null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
