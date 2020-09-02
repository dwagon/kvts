""" Timesheet views """
# pylint: disable=relative-beyond-top-level
from django.shortcuts import render, redirect
from .models import Person, Day, Interval, Fortnight
from .forms import NormalHoursForm, IntervalFormSet


##############################################################################
def index(request):
    """ Front Page """
    people_list = Person.objects.all()
    context = {'people': people_list}
    return render(request, 'index.template', context)


##############################################################################
def person_view(request, person_id):
    """ Details about a person """
    fort = Fortnight.objects.get(current=True)
    day_list = Day.objects.filter(person=person_id, fortnight=fort).order_by('day')
    person = Person.objects.get(pk=person_id)
    context = {'person': person, 'days': day_list}
    return render(request, 'person.template', context)


##############################################################################
def handle_interval_form(interval_form, day_id):
    """ Handle a valid interval form submission """
    day = Day.objects.get(pk=day_id)
    for form in interval_form:
        if form.has_changed():
            hours = form.cleaned_data['hours'] * 4
            worktype = form.cleaned_data['worktype']
            if hours == 0:
                try:
                    oldint = Interval.objects.get(
                        day=day_id,
                        worktype=worktype
                    )
                    oldint.delete()
                except Interval.DoesNotExist:
                    pass
            else:
                inter, _ = Interval.objects.get_or_create(
                    day=day,
                    worktype=worktype,
                    quarterhours=hours
                )
                inter.save()


##############################################################################
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
            handle_interval_form(interval_form, day_id)
            interval_list = Interval.objects.filter(day=day_id).order_by('day')
        else:
            print(f"Naughty={interval_form.errors=}")
            print(f"Naughty={interval_form.total_error_count()}")
            print(f"Naughty={interval_form.non_form_errors()}")
        return redirect('personday', person_id=person_id, day_id=day_id)

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
