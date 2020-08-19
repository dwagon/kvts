""" Timesheet views """
from django.shortcuts import render
from .models import Person, Day, Interval, Fortnight
from .forms import NormalHoursForm, IntervalFormSet


def index(request):
    """ Front Page """
    people_list = Person.objects.all()
    context = {'people': people_list}
    return render(request, 'index.template', context)


def person_view(request, person_id):
    """ Details about a person """
    fort = Fortnight.objects.get(current=True)
    day_list = Day.objects.filter(person=person_id, fortnight=fort).order_by('day')
    person = Person.objects.get(pk=person_id)
    context = {'person': person, 'days': day_list}
    return render(request, 'person.template', context)


def personday_view(request, person_id, day_id):
    """ Details about a day for a particular person"""
    interval_list = Interval.objects.filter(day=day_id).order_by('day')
    person = Person.objects.get(pk=person_id)
    day = Day.objects.get(pk=day_id)
    init_int = [{'worktype': _.worktype, 'hours': _.quarterhours / 4.0} for _ in interval_list]

    if request.method == 'POST':
        hours_form = NormalHoursForm(request.POST)
        if hours_form.is_valid():
            hours = hours_form.cleaned_data['norm']
            day.normal_quarterhours = hours * 4
            day.save()
        interval_form = IntervalFormSet(request.POST, initial=init_int)
        if interval_form.is_valid():
            for form in interval_form:
                if form.has_changed():
                    hours = form.cleaned_data['hours'] * 4
                    worktype = form.cleaned_data['worktype']
                    if hours == 0:
                        oldint = Interval.objects.get(
                            day=day_id,
                            worktype=worktype
                        )
                        oldint.delete()
                    else:
                        newint = Interval(
                            day=day,
                            quarterhours=hours,
                            worktype=worktype
                        )
                        newint.save()

    else:
        hours_form = NormalHoursForm(initial={'norm': day.normal_quarterhours / 4})
        interval_form = IntervalFormSet(initial=init_int)

    context = {
        'person': person,
        'day': day,
        'intervals': interval_list,
        'hours_form': hours_form,
        'interval_form': interval_form
    }
    return render(request, 'personday.template', context)

# EOF
