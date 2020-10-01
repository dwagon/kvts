""" Forms for timesheets """
# pylint: disable=relative-beyond-top-level

from django import forms


##############################################################################
class FortnightForm(forms.Form):
    """ Forms handling for the Fortnight model """
    notes = forms.CharField(widget=forms.Textarea)


##############################################################################
class VetDayForm(forms.Form):
    """ Form handling the details of a day """
    normal = forms.DecimalField(
        max_value=24,
        min_value=0,
        decimal_places=1, required=False
    )
    worked = forms.DecimalField(
        max_value=24,
        min_value=0,
        decimal_places=1, required=False
    )
    sick = forms.DecimalField(
        max_value=24,
        min_value=0,
        decimal_places=1, required=False
    )
    leave = forms.DecimalField(
        max_value=24,
        min_value=0,
        decimal_places=1, required=False
    )
    public = forms.DecimalField(
        max_value=24,
        min_value=0,
        decimal_places=1, required=False
    )
    study = forms.DecimalField(
        max_value=24,
        min_value=0,
        decimal_places=1, required=False
    )
    notes = forms.CharField(widget=forms.Textarea)


##############################################################################
class NurseDayForm(forms.Form):
    """ Form handling the details of a day """
    normal = forms.DecimalField(
        max_value=24,
        min_value=0,
        decimal_places=1, required=False
    )
    worked = forms.DecimalField(
        max_value=24,
        min_value=0,
        decimal_places=1, required=False
    )
    sick = forms.DecimalField(
        max_value=24,
        min_value=0,
        decimal_places=1, required=False
    )
    leave = forms.DecimalField(
        max_value=24,
        min_value=0,
        decimal_places=1, required=False
    )
    public = forms.DecimalField(
        max_value=24,
        min_value=0,
        decimal_places=1, required=False
    )
    notes = forms.CharField(widget=forms.Textarea)

# EOF
