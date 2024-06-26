# Generated by Django 4.2.12 on 2024-05-10 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.CharField(max_length=100, verbose_name='Текст')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Фото')),
                ('video', models.URLField(blank=True, null=True, verbose_name='Видео')),
                ('time_new', models.PositiveIntegerField(verbose_name='Время')),
                ('music', models.FileField(blank=True, null=True, upload_to='audio/', verbose_name='Песню')),
                ('author', models.CharField(max_length=100, null=True, verbose_name='Афтор')),
                ('category', models.CharField(choices=[('Спорт', 'Спорт'), ('Бизнес', 'Бизнес'), ('Шоу бизнес', 'Шоу бизнес'), ('Мир', 'Мир')], max_length=100, verbose_name='Выберите категорю')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
