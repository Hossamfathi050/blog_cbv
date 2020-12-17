# Generated by Django 3.1.4 on 2020-12-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, unique=True)),
                ('content', models.TextField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=True)),
                ('email', models.EmailField(blank=True, max_length=253, null=True)),
                ('view_count', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('prim', 'المرحلة الابتدائية'), ('mid', 'المرحلة المتوسطة'), ('gen', 'عام'), ('sec', 'المرحلة الثانوية')], max_length=3500)),
            ],
        ),
    ]
