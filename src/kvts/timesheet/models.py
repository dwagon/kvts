""" Model definition for KVTS """
from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _


##############################################################################
class Fortnight(models.Model):
    """ Period of timesheet """
    start = models.DateField()

    def __str__(self):
        return str(self.start)


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
    normal_quarterhours = models.PositiveIntegerField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.person} @ {self.day}"

    def all_hours(self, typ_='N'):
        """ Calculate all hours allocated today """
        tots = 0
        ivals = Interval.objects.filter(day=self)   # pylint: disable=no-member
        if typ_:
            ivals = ivals.filter(worktype=typ_)
        for iv in ivals:
            tots += iv.quarterhours
        return tots

    def overtime(self):
        """ Number of quarter hours at 1.5 (Max 3 hours) """
        if self.all_hours() - self.normal_quarterhours > 0:
            return min(12, self.all_hours() - self.normal_quarterhours)
        else:
            return 0

    def doubletime(self):
        """ Number of quarter hours at 2.0 (Max 3 hours) """
        if self.all_hours() - self.normal_quarterhours - self.overtime() > 0:
            return self.all_hours() - self.normal_quarterhours - self.overtime()
        else:
            return 0

    def normal(self):
        """ Return quarterhours at normal pay rate """
        return min(self.all_hours(), self.normal_quarterhours)

    def total(self):
        """ Return the equivalent hours to be paid """
        return self.normal() + Decimal(1.5) * self.overtime() + Decimal(2.0) * self.doubletime()

    def weekday(self):
        """ Return day of the week """
        return self.day.strftime("%a")  # pylint: disable=no-member


##############################################################################
class Interval(models.Model):
    """ Work Interval """
    class IntervalChoices(models.TextChoices):
        """ Types of Work Interval """
        NORMAL = 'N', _('Working')
        SICK = 'S', _('Sick Leave')
        LEAVE = 'L', _('Paid Leave')
        PUBLIC_HOLIDAY = 'P', _('Public Holiday')
        STUDY = 'Z', _('Sudy Leave')
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    quarterhours = models.PositiveIntegerField()
    worktype = models.CharField(
        max_length=1,
        choices=IntervalChoices.choices,
        default=IntervalChoices.NORMAL
    )

    def work(self):
        """ Return work type in human """
        return self.get_worktype_display()  # pylint: disable=no-member

    def __str__(self):
        return f"{self.quarterhours/4} hours of {self.work()} on {self.day}"

    def hours(self):
        """ Return quarterhours in human """
        return self.quarterhours / 4.0


# EOF
