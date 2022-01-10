from django.db import models


class Physic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PsychicNumbers(models.Model):
    """Модель для хранения ответов экстрасенсов'"""
    psychic = models.ForeignKey(
        Physic,
        on_delete=models.CASCADE,
        related_name='psychic'
    )
    user_session = models.CharField(max_length=50)
    # user_attempt = models.IntegerField(default=0)
    number = models.SmallIntegerField()
    confidence_level = models.IntegerField(default=0)


class UserNumbers(models.Model):
    """Модель для хранения загаданных чисел пользователя"""
    user_session = models.CharField(max_length=50)
    # user_attempt = models.IntegerField(default=0)
    number = models.SmallIntegerField(verbose_name='Число')
