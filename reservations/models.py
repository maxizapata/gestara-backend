from django.db import models
from cooperatives.models import Cooperative


class AllowReservation(models.Model):
    cooperative = models.ForeignKey(
        Cooperative,
        on_delete=models.DO_NOTHING,
        limit_choices_to={'category': 9},
        blank=True,
    )
    allow_reservation = models.BooleanField(default=True)

    def __str__(self):
        return str(self.cooperative)


class Reservation(models.Model):
    REQUESTED = 'REQUESTED'
    REPROGRAMED = 'REPROGRAMED'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'
    STATUSES = (
        (REQUESTED, REQUESTED),
        (REPROGRAMED, REPROGRAMED),
        (COMPLETED, COMPLETED),
        (CANCELED, CANCELED),
    )

    cooperative = models.ForeignKey(
        AllowReservation,
        on_delete=models.DO_NOTHING,
        blank=True
    )
    datetime = models.DateTimeField(null=True)
    diners = models.IntegerField(default=1)
    status = models.CharField(
        max_length=20, choices=STATUSES, default=REQUESTED)

    def __str__(self):
        return str(self.cooperative)
