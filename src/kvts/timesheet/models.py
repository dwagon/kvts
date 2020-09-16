""" Model definition for KVTS """
from decimal import Decimal
import datetime
from django.db import models
from django.contrib.auth.models import User     # pylint: disable=imported-auth-user


##############################################################################
class Fortnight(models.Model):
    """ Period of timesheet """
    start = models.DateField()
    current = models.BooleanField(default=False, unique=True)

    def __str__(self):
        return f"Fortnight starting {str(self.start)} - current {self.current}"

    def save(self, *args, **kwargs):    # pylint: disable=signature-differs
        super().save(*args, **kwargs)
        if self.current:
            self.create_all_fortnight()

    def create_person_fortnight(self, user):
        """ Create blank dates for a user """
        day = self.start
        person_days = Day.objects.filter(person=user)
        for __ in range(14):
            person_days.get_or_create(person=user, day=day, fortnight=self)
            day += datetime.timedelta(days=1)

    def create_all_fortnight(self):
        """ Create blank dates for everyone """
        for person in User.objects.all():
            self.create_person_fortnight(person)


##############################################################################
class Day(models.Model):
    """ A Day """
    day = models.DateField()
    normal_qh = models.PositiveIntegerField(default=8*4)
    person = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fortnight = models.ForeignKey(Fortnight, on_delete=models.CASCADE)
    worked_qh = models.PositiveIntegerField(default=0)
    sick_qh = models.PositiveIntegerField(default=0)
    leave_qh = models.PositiveIntegerField(default=0)
    publich_qh = models.PositiveIntegerField(default=0)
    study_qh = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.person} @ {self.day}"

    def overtime(self):
        """ Number of quarter hours at 1.5 (Max 3 hours) """
        if self.worked_qh - self.normal_qh > 0:
            return min(12, self.worked_qh - self.normal_qh)
        return 0

    def doubletime(self):
        """ Number of quarter hours at 2.0 (Max 3 hours) """
        if self.worked_qh - self.normal_qh - self.overtime() > 0:
            return self.worked_qh - self.normal_qh - self.overtime()
        return 0

    def normal(self):
        """ Return quarterhours at normal pay rate """
        return min(self.worked_qh, self.normal_qh)

    def total(self):
        """ Return the equivalent hours to be paid """
        return self.normal() + Decimal(1.5) * self.overtime() + Decimal(2.0) * self.doubletime()

    def weekday(self):
        """ Return day of the week """
        return self.day.strftime("%a")

# EOF
