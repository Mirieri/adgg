from rest_framework import viewsets
from django_tables2.views import SingleTableView
from django_tables2.export.views import ExportMixin
from django_filters.views import FilterView
from djgeojson.views import GeoJSONLayerView

from .models import Reg02Maininfo, Reg01Lkpmaindistrict, Reg04Maininfo
from .tables import Reg02MaininfoTable
from .filters import Reg02MaininfoFilter
from .serializers import (
    Reg02MaininfoSerializer,
    Reg01LkpmaindistrictSerializer,
    Reg04MaininfoSerializer
)


class Reg02MaininfoView(FilterView, ExportMixin, SingleTableView):
    model = Reg02Maininfo
    table_class = Reg02MaininfoTable
    filterset_class = Reg02MaininfoFilter
    template_name = 'animalregistration/reg02maininfo_list.html'
    queryset = Reg02Maininfo.objects.filter(surveyid__isnull=False)

#class Reg02MaininfoGeoPoinView(GeoJSONLayerView):
#    model = Reg02Maininfo
#    queryset = Reg02Maininfo.objects.values_list('farmername','farmermobile','gpsloc')
    
class Reg02MaininfoViewSet(viewsets.ModelViewSet):
    queryset = Reg02Maininfo.objects.all()
    serializer_class = Reg02MaininfoSerializer


class Reg01LkpmaindistrictViewSet(viewsets.ModelViewSet):
    queryset = Reg01Lkpmaindistrict.objects.all()
    serializer_class = Reg01LkpmaindistrictSerializer
    lookup_field = 'maindistrict_des'


class Reg04MaininfoViewSet(viewsets.ModelViewSet):
    queryset = Reg04Maininfo.objects.all()
    serializer_class = Reg04MaininfoSerializer
    lookup_field = 'hh'
