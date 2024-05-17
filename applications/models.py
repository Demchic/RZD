from django.contrib.auth import get_user_model
from django.db import models

class DoneManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Articles.Status.DONE)


user = get_user_model()
class Articles(models.Model):
    class Status(models.IntegerChoices):
        NEW = 0, 'Новая'
        DONE = 1, 'Выполненная'

    ch = "Выберите услугу"
    internet = "Интернет"
    telephone = "Телефония"
    service_choices = {
      ch: 'Выберите услугу', internet: 'Интернет', telephone: 'Телефония'
    }
    objects = None
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    department = models.CharField('Департамент', max_length=10)
    sector = models.CharField('Полное наименование отдела/сектора', max_length=50, null=False, blank=False)
    post = models.CharField('Должность', max_length=100, null=False, blank=False)
    surname = models.CharField('Фамилия', max_length=30)
    name = models.CharField('Имя', max_length=30)
    middle_name = models.CharField('Отчество', max_length=30)
    tab_number = models.CharField('Табельный номер', max_length=7, null=False, blank=False)
    mail = models.EmailField('Рабочая почта', max_length=30)
    phone_number = models.CharField('Рабочий телефон', max_length=12)
    service = models.CharField('Услуга', max_length=20, choices=service_choices, default=ch)
    address = models.CharField('Адрес установки оборудования', max_length=30, null=False, blank=False)
    date = models.DateTimeField(auto_now=True, verbose_name='Дата составления заявки')
    komm = models.TextField('Комментарий')
    status = models.BooleanField('Статус заявки', choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                                                default=Status.NEW)

    def __str__(self):
        return self.service

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'
