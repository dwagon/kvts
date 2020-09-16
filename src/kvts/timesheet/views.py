""" Timesheet views """
# pylint: disable=relative-beyond-top-level
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User     # pylint: disable=imported-auth-user
from .models import Day, Fortnight
from .forms import DayForm


##############################################################################
@login_required
def index(request):
    """ Front Page """
    print(f"user={request.user}")
    if request.user.is_superuser:
        people_list = User.objects.all()
    else:
        people_list = User.objects.get(name=request.user)
    context = {'people': people_list}
    return render(request, 'index.template', context)


##############################################################################
@login_required
def person_view(request, person_id):
    """ Details about a person """
    fort = Fortnight.objects.get(current=True)
    day_list = Day.objects.filter(person=person_id, fortnight=fort).order_by('day')
    person = User.objects.get(pk=person_id)
    context = {'person': person, 'days': day_list}
    return render(request, 'person.template', context)


##############################################################################
def handle_day_form(request, day):
    """ Handle the day form """
    form = DayForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        day.normal_qh = 4 * data['normal'] if data['normal'] else 0
        day.worked_qh = 4 * data['worked'] if data['worked'] else 0
        day.sick_qh = 4 * data['sick'] if data['sick'] else 0
        day.leave_qh = 4 * data['leave'] if data['leave'] else 0
        day.publich_qh = 4 * data['public'] if data['public'] else 0
        day.study_qh = 4 * data['study'] if data['study'] else 0
        day.save()


##############################################################################
@login_required
def personday_view(request, person_id, day_id):
    """ Details about a day for a particular person"""
    person = User.objects.get(pk=person_id)
    day = Day.objects.get(pk=day_id)

    if request.method == 'POST':
        handle_day_form(request, day)
        return redirect('person', person_id=person_id)
    form = DayForm(
        initial={
            'normal': day.normal_qh / 4,
            'worked': day.worked_qh / 4,
            'sick': day.sick_qh / 4,
            'leave': day.leave_qh / 4,
            'public': day.publich_qh / 4,
            'study': day.study_qh / 4,
            }
        )

    context = {
        'person': person,
        'day': day,
        'form': form,
    }
    return render(request, 'personday.template', context)

# EOF
