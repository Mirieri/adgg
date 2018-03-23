from django.forms import widgets

import django_filters as filters

from .models import Reg02Maininfo
from . import constants


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
        method='filter_subset_animal_categories',
        help_text='Hold CTRL button to select multiple entries'
    )
    animcatowned_exact = filters.MultipleChoiceFilter(
        label='Animal categories exactly owned at farm',
        choices=constants.ANIMAL_CATEGORIES,
        method='filter_exact_animal_categories',
        help_text='Hold CTRL button to select multiple entries'
    )

    class Meta:
        model = Reg02Maininfo
        fields = ('regdate', 'farmername', 'farmermobile', 'hhhname', 'hhhmobile','hhhgender', 'animcatowned_exact',
                  'hh_district', 'farmerhhhead',
                 )
        #exclude = ('surveyid', 'deviceid', 'originid', 'icow', 'rowuuid', 
        #           'start_time', 'end_time', 'farmerhhhead', 'nmale0to5',
        #           'nfem0to5', 'nmale6to14', 'nfem6to14', 'nmale15to64',
        #           'nmaleo65', 'nfemo65', 'nfem15to64', 'gpsloc', 'welcomesent',
        #           'apologysent')

    def filter_subset_animal_categories(self, queryset, name, value):
        items = [item.pk for item in queryset if set(value).issubset(item.animals_categories_numbers)]
        return queryset.filter(pk__in=items)

    def filter_exact_animal_categories(self, queryset, name, value):
        items = [item.pk for item in queryset if set(value) == set(item.animals_categories_numbers)]
        return queryset.filter(pk__in=items)
        
        
