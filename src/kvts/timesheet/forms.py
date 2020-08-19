""" Forms for timesheets """
from django import forms
from django.forms import formset_factory
from .models import IntervalChoices


class NormalHoursForm(forms.Form):
    """ Set number of normal hours in a day """
    norm = forms.DecimalField(label="Normal Hours", min_value=0.0, max_value=24.0, decimal_places=1)


class IntervalForm(forms.Form):
    """ Enter interval data """
    worktype = forms.ChoiceField(choices=IntervalChoices.choices)
    hours = forms.DecimalField(min_value=0.0, max_value=24.0)


IntervalFormSet = formset_factory(IntervalForm, extra=1)

# EOF
