import django_filters as filters

from .models import Reg02Maininfo

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
     class Meta:
         model = Reg02Maininfo
         exclude = ('surveyid', 'deviceid', 'originid', 'icow', 'rowuuid', 'start_time', 'end_time', 'farmerhhhead')
