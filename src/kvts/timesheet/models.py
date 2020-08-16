""" Model definition for KVTS """
from django.db import models
from django.utils.translation import gettext_lazy as _


##############################################################################
class Person(models.Model):
    """ Person """
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


##############################################################################
class Day(models.Model):
    """ A Day """
    day = models.DateField()
    normal_quarterhours = models.IntegerField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.day)


##############################################################################
class Interval(models.Model):
    """ Work Interval """
    class IntervalChoices(models.TextChoices):
        """ Types of Work Interval """
        NORMAL = 'N', _('Normal')
        SICK = 'S', _('Sick Leave')
        LEAVE = 'L', _('Paid Leave')
        PUBLIC_HOLIDAY = 'P', _('Public Holiday')
        STUDY = 'Z', _('Sudy Leave')
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    quarterhours = models.IntegerField()
    worktype = models.CharField(
        max_length=1,
        choices=IntervalChoices.choices,
        default=IntervalChoices.NORMAL
    )

    def __str__(self):
        return f"{self.quarterhours/4} hours of {self.get_worktype_display()} on {self.day}"

    def hours(self):
        """ Return quarterhours in human """
        return self.quarterhours / 4.0

# EOF
