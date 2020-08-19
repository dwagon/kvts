""" Timesheet views """
import datetime
from django.shortcuts import render
from .models import Person, Day, Interval, Fortnight
from .forms import NormalHoursForm


def index(request):
    """ Front Page """
    people_list = Person.objects.all()
    context = {'people': people_list}
    return render(request, 'index.template', context)


def person_view(request, person_id):
    """ Details about a person """
    day_list = Day.objects.filter(person=person_id).order_by('day')
    person = Person.objects.get(pk=person_id)
    context = {'person': person, 'days': day_list}
    return render(request, 'person.template', context)


def personday_view(request, person_id, day_id):
    """ Details about a day for a particular person"""
    interval_list = Interval.objects.filter(day=day_id).order_by('day')
    person = Person.objects.get(pk=person_id)
    day = Day.objects.get(pk=day_id)

    if request.method == 'POST':
        form = NormalHoursForm(request.POST)
        if form.is_valid():
            hours = form.cleaned_data['norm']
            day.normal_quarterhours = hours * 4
            day.save()
    else:
        form = NormalHoursForm(initial={'norm': day.normal_quarterhours / 4})

    context = {'person': person, 'day': day, 'intervals': interval_list, 'form': form}
    return render(request, 'personday.template', context)

# EOF
