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
    number = models.SmallIntegerField()
    is_checked = models.BooleanField(default=False)
    confidence_level = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.psychic.name} {self.number} {self.confidence_level=}"


class UserNumbers(models.Model):
    """Модель для хранения загаданных чисел пользователя"""
    user_session = models.CharField(max_length=50)
    is_checked = models.BooleanField(default=False)
    number = models.SmallIntegerField(verbose_name='Число')

    def __str__(self):
        return f"{self.user_session} {self.number}"
