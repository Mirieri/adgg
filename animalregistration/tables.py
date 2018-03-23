import django_tables2 as tables

from .models import Reg02Maininfo


class Reg02MaininfoTable(tables.Table):
    class Meta:
        model = Reg02Maininfo
        template_name = 'animalregistration/bootstrap-responsive.html'

    def render_animcatowned(self, record):
        if record.animals_categories_owned is not None:
            return ', '.join(record.animals_categories_owned)
        return record.animals_categories_owned
