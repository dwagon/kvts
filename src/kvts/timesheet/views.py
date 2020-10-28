""" Timesheet views """
# pylint: disable=relative-beyond-top-level
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Day, Fortnight, Employee, EmployeeFortnight
from .forms import NurseDayForm, VetDayForm, FortnightForm


##############################################################################
@login_required
def index(request):
    """ Front Page """
    person = Employee.objects.get(pk=request.user.id)
    if request.user.is_superuser:
        people_list = Employee.objects.all()
    else:
        people_list = [Employee.objects.get(username=request.user)]
    context = {
        'people': people_list,
        'person': person,
        }
    return render(request, 'index.template', context)


##############################################################################
@login_required
def person_view(request, person_id):
    """ Details about a person """
    fort = Fortnight.objects.get(current=True)
    person = Employee.objects.get(pk=person_id)
    userfort, _ = EmployeeFortnight.objects.get_or_create(
        person=person, notes='', fortnight=fort
        )
    if request.method == 'POST':
        form = FortnightForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            userfort.notes = data['notes']
            userfort.save()

    day_list = Day.objects.filter(person=person_id, fortnight=fort).order_by('day')
    if not day_list:
        fort.create_person_fortnight(person)
    form = FortnightForm(initial={'notes': userfort.notes})
    context = {
        'person': person,
        'days': day_list,
        'fortnight': fort,
        'form': form,
        'userfort': userfort
    }
    return render(request, 'person.template', context)


##############################################################################
def handle_day_form(request, day, person):
    """ Handle the day form """
    if person.is_vet:
        form = VetDayForm(request.POST)
    else:
        form = NurseDayForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        day.normal_qh = 4 * data['normal'] if data['normal'] else 0
        day.worked_qh = 4 * data['worked'] if data['worked'] else 0
        day.sick_qh = 4 * data['sick'] if data['sick'] else 0
        day.leave_qh = 4 * data['leave'] if data['leave'] else 0
        day.publich_qh = 4 * data['public'] if data['public'] else 0
        if person.is_vet:
            day.study_qh = 4 * data['study'] if data['study'] else 0
        else:
            day.dtudy_qh = 0
        day.notes = data['notes']
        day.save()


##############################################################################
@login_required
def personday_view(request, person_id, day_id):
    """ Details about a day for a particular person"""
    person = Employee.objects.get(pk=person_id)
    day = Day.objects.get(pk=day_id)
    initial = {
        'normal': day.normal_qh / 4,
        'worked': day.worked_qh / 4,
        'sick': day.sick_qh / 4,
        'leave': day.leave_qh / 4,
        'public': day.publich_qh / 4,
        'notes': day.notes,
        }
    if person.is_vet:
        use_form = VetDayForm
        initial['study'] = day.study_qh / 4
    else:
        use_form = NurseDayForm

    if request.method == 'POST':
        handle_day_form(request, day, person)
        return redirect('person', person_id=person_id)
    form = use_form(initial=initial)

    context = {
        'person': person,
        'day': day,
        'form': form,
    }
    return render(request, 'personday.template', context)

# EOF
