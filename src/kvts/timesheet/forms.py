""" Forms for timesheets """
from django import forms


class NormalHoursForm(forms.Form):
    """ Set number of normal hours in a day """
    norm = forms.DecimalField(label="Normal Hours", min_vaue=0.0, max_value=24.0, decimal_places=1)
