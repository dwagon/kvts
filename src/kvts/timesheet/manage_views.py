""" Timesheet Management views """
# pylint: disable=relative-beyond-top-level
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Fortnight
from .forms import ManageFortnightForm


##############################################################################
@login_required
def index(request):
    """ Front Management Page """
    context = {'people': []}
    return render(request, 'index.template', context)


##############################################################################
@login_required
def current_fortnight(request, fortnight_id):
    """ Make the specified fortnight current """
    instance = get_object_or_404(Fortnight, id=fortnight_id)
    instance.make_current()
    return redirect('manage_fortnights')


##############################################################################
@login_required
def delete_fortnight(request, fortnight_id):
    """ Delete a fortnight """
    print(fortnight_id)


##############################################################################
@login_required
def create_fortnight(request):
    """ Create a new fortnight """
    form = ManageFortnightForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('manage_fortnights')
    context = {
        'form': form,
    }
    return render(request, 'create_fortnight.template', context)


##############################################################################
def edit_fortnight(request, fortnight_id):
    """ Manage the manage fortnight form """
    instance = get_object_or_404(Fortnight, id=fortnight_id)
    form = ManageFortnightForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('manage_fortnights')
    context = {
        'form': form,
        'fort': instance
    }
    return render(request, 'edit_fortnight.template', context)


##############################################################################
@login_required
def fortnight(request):
    """ Manage details about fortnights """
    fortnights = Fortnight.objects.all()
    context = {
        'fortnights': fortnights
    }
    return render(request, 'manage_fortnight.template', context)


##############################################################################
@login_required
def user(request):
    """ Manage details about users """
    context = {}
    return render(request, 'personday.template', context)

# EOF
