import django_tables2 as tables

from .models import Reg02Maininfo


class Reg02MaininfoTable(tables.Table):
    class Meta:
        model = Reg02Maininfo
        template_name = 'animalregistration/bootstrap-responsive.html'
