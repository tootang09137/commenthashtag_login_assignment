# Generated by Django 4.0.4 on 2022-07-19 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('blog_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.post')),
            ],
        ),
    ]