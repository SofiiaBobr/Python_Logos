from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Post(models.Model):
    # Назва статті або запису.
    title = models.CharField(max_length=50)

    # Текстове поле для зберігання великих обсягів текстової інформації, такої як контент статті.
    text = models.TextField(max_length=1000)

    # Дата і час створення запису. За замовчуванням встановлено поточний момент часу при створенні запису.
    create_date = models.DateTimeField(default=timezone.now())

    # Зовнішній ключ, який посилається на користувача, який є автором запису. Видаляється, якщо користувач видаляється.
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Прапорець, що вказує, чи опубліковано запис. За замовчуванням встановлено на False (не опубліковано).
    published = models.BooleanField(default=False)


    def __str__(self):
        return self.title
