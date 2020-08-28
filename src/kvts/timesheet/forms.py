""" Forms for timesheets """
# pylint: disable=relative-beyond-top-level

from django.core.exceptions import ValidationError
from django import forms
from django.forms import formset_factory
from .models import IntervalChoices


##############################################################################
class NormalHoursForm(forms.Form):
    """ Set number of normal hours in a day """
    norm = forms.DecimalField(label="Normal Hours", min_value=0.0, max_value=24.0, decimal_places=1)


##############################################################################
class IntervalForm(forms.Form):
    """ Enter interval data """
    worktype = forms.ChoiceField(choices=IntervalChoices.choices)
    hours = forms.DecimalField(min_value=0.0, max_value=24.0)

    def clean_hours(self):
        """ Ensure hours is a reasonable number """
        hours = self.cleaned_data['hours']
        return hours


##############################################################################
class BaseIntervalFormSet(forms.BaseFormSet):
    """ Allow for validation of consistency across all the forms """
    def clean(self):
        if any(self.errors):
            return
        seen = set()
        for form in self.forms:
            worktype = form.cleaned_data.get('worktype')
            if worktype in seen:
                raise ValidationError("Can only have the same work type once per day")
            seen.add(worktype)


##############################################################################
IntervalFormSet = formset_factory(IntervalForm, BaseIntervalFormSet)

# EOF
