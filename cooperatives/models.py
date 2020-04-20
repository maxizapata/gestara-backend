from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    class Meta:
        verbose_name_plural = ("Categories")
    name = models.CharField(max_length=50)
    name_pretty = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Cooperative(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)
    short_description = models.CharField(max_length=40)
    description = models.TextField(max_length=1000)
    logo = models.ImageField(upload_to='./pictures/cooperatives/',
                             default='pictures/generic/no_logo.png')
    phone = PhoneNumberField(blank=True)
    web = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=150, blank=True)
    instagram = models.CharField(max_length=150, blank=True)
    skype = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=50, blank=True)
    map_latitude = models.DecimalField(max_digits=9,
                                       decimal_places=7, blank=True)
    map_longitude = models.DecimalField(max_digits=9,
                                        decimal_places=7, blank=True)
    whatsapp = PhoneNumberField(blank=True)
   category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Timetable(models.Model):
    cooperative = models.ForeignKey(
        Cooperative,
        on_delete=models.DO_NOTHING,
        limit_choices_to={'category': 9}
    )
    monday_open = models.TimeField(blank=True, null=True)
    monday_close = models.TimeField(blank=True, null=True)
    tuesday_open = models.TimeField(blank=True, null=True)
    tuesday_close = models.TimeField(blank=True, null=True)
    wednesday_open = models.TimeField(blank=True, null=True)
    wednesday_close = models.TimeField(blank=True, null=True)
    thursday_open = models.TimeField(blank=True, null=True)
    thursday_close = models.TimeField(blank=True, null=True)
    friday_open = models.TimeField(blank=True, null=True)
    friday_close = models.TimeField(blank=True, null=True)
    saturday_open = models.TimeField(blank=True, null=True)
    saturday_close = models.TimeField(blank=True, null=True)
    sunday_open = models.TimeField(blank=True, null=True)
    sunday_close = models.TimeField(blank=True, null=True)
