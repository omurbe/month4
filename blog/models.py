from django.db import models

class BlogModels(models.Model):
    CATEGORY_NEWS = (
        ('Спорт', 'Спорт'),
        ('Бизнес', 'Бизнес'),
        ('Шоу бизнес', 'Шоу бизнес'),
        ('Мир', 'Мир')
    )

    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Текст')
    image = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='Фото')
    video = models.URLField(verbose_name='Видео', null=True, blank=True)
    time_new = models.PositiveIntegerField(verbose_name='Время')
    music = models.FileField(upload_to='audio/', verbose_name='Песню', null=True, blank=True)
    author = models.CharField(max_length=100, verbose_name='Афтор', null=True)
    category = models.CharField(max_length=100, choices=CATEGORY_NEWS, verbose_name='Выберите категорю')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    blog = models.ForeignKey(BlogModels,
                             related_name='reviews',
                             on_delete=models.CASCADE)
    stars = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.blog.title}"




