from django.forms import widgets

import django_filters as filters

from .models import Reg02Maininfo
from . import constants
from .forms import OptionsForm


class Reg02MaininfoFilter(filters.FilterSet):
    regdate = filters.DateFromToRangeFilter(
        widget = filters.widgets.RangeWidget(
            attrs = {'class':'datepicker'}
        )
    )
    farmername = filters.CharFilter(
        label = 'Farmername Auto Search',
        lookup_expr='icontains'
    )
    farmermobile = filters.CharFilter(
        lookup_expr='icontains'
    )
    hhhname = filters.CharFilter(
        lookup_expr='icontains'
    )
    hhhmobile = filters.CharFilter(
        lookup_expr='icontains'
    )
    #nmale0to5 = filters.NumberFilter(
    #    widget=widgets.NumberInput(       
    #        attrs={'min':0,'max':5}
    #    )
    #)
    animcatowned = filters.MultipleChoiceFilter(
        label='Animal categories owned at farm',
        choices=constants.ANIMAL_CATEGORIES,
        method='filter_animal_categories',
        help_text='Hold CTRL button to select multiple entries'
    )
    hhproblems = filters.MultipleChoiceFilter(
        label='House Hold Problem',
        choices=constants.HOUSE_HOLD_PROBLEMS,
        method='filter_household_problems',
        help_text='Hold CTRL button to select multiple entriess'
    )
    hhproblemsoth = filters.CharFilter(
        label='Other House Hold Problem',
        lookup_expr='icontains',
    )
    #animcatowned_exact = filters.MultipleChoiceFilter(
    #    label='Animal categories exactly owned at farm',
    #    choices=constants.ANIMAL_CATEGORIES,
    #    method='filter_exact_animal_categories',
    #    help_text='Hold CTRL button to select multiple entries'
    #)

    class Meta:
        model = Reg02Maininfo
        #fields = ('regdate', 'farmername', 'farmermobile', 'hhhname', 'hhhmobile','hhhgender',
        #          'hh_district', 'farmerhhhead',
        #         )
        exclude = ('surveyid', 'deviceid', 'originid', 'icow', 'rowuuid', 
                   'start_time', 'end_time', 'farmerhhhead', 'nmale0to5',
                   'nfem0to5', 'nmale6to14', 'nfem6to14', 'nmale15to64',
                   'nmaleo65', 'nfemo65', 'nfem15to64', 'gpsloc', 'welcomesent',
                   'apologysent', 'inpaidbundle', 'inadggbundle')
        form = OptionsForm

    def filter_animal_categories(self, queryset, name, value):
        option = self.data['options']
        if option == 'e':
            items = [item.pk 
            for item in queryset 
                if set(value) == set(item.animals_categories_numbers)]
        elif option == 'a':
            items = [item.pk 
            for item in queryset 
                if set(value).issubset(item.animals_categories_numbers)]
        elif option == 'o':
            items = []
            for item in queryset:
                for el in value:
                    if el in item.animals_categories_numbers:
                        items.append(item.pk)
        return queryset.filter(pk__in=items)

    def filter_household_problems(self, queryset, name, value):
        option = self.data['options']
        if option == 'e':
            items = [item.pk 
            for item in queryset 
                if set(value) == set(item.house_hold_problem_numbers)]
        elif option == 'a':
            items = [item.pk 
            for item in queryset 
                if set(value).issubset(item.house_hold_problem_numbers)]
        elif option == 'o':
            items = []
            for item in queryset:
                for el in value:
                    if el in item.house_hold_problem_numbers:
                        items.append(item.pk)
        return queryset.filter(pk__in=items)

    #def filter_exact_animal_categories(self, queryset, name, value):
    #    items = [item.pk for item in queryset if set(value) == set(item.animals_categories_numbers)]
    #    return queryset.filter(pk__in=items)
        
        
