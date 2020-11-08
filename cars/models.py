from django.db import models
from django.db.models import Q
from colorfield.fields import ColorField
import operator
from functools import reduce

# Create your models here.
class Car(models.Model):
    TRANSMISSION_MANUAL = 1
    TRANSMISSION_AUTOMATIC = 2
    TRANSMISSION_ROBOTIC = 3
    TRANSMISSION_CHOICES = [
            (TRANSMISSION_MANUAL, "механика"),
            (TRANSMISSION_AUTOMATIC, "автомат"),
            (TRANSMISSION_ROBOTIC, "робот"),
    ]
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    issue_year = models.IntegerField()
    transmission = models.SmallIntegerField(choices=TRANSMISSION_CHOICES)
    color = ColorField(blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return "{} {} ({}) {}".format(
                self.manufacturer,
                self.model,
                self.issue_year,
                self.get_transmission_display())

    @staticmethod
    def get_filter(params):
        manufacturer = params.get('manufacturer')
        model = params.get('model')
        issue_year = params.get('issue_year')
        transmission = params.get('transmission')
        color = params.get('color')

        q_list = []
        if manufacturer:
            q_list.append(Q(manufacturer__icontains=manufacturer))
        if model:
            q_list.append(Q(model__icontains=model))
        if issue_year:
            q_list.append(Q(issue_year=issue_year))
        if transmission:
            q_list.append(Q(transmission=transmission))
        if color:
            q_list.append(Q(color=color))

        return reduce(operator.and_, q_list, Q())



