import django_tables2 as tables

from .models import Reg02Maininfo


class Reg02MaininfoTable(tables.Table):
    gpsloc = tables.TemplateColumn(
        verbose_name='GPS location',
        template_name='animalregistration/gpsloc_column.html'
    )

    class Meta:
        model = Reg02Maininfo
        template_name = 'animalregistration/bootstrap-responsive.html'
        exclude = ('deviceid', 'surveyid','originid')

    def render_animcatowned(self, record):
        if record.animals_categories_owned is not None:
            return ', '.join(record.animals_categories_owned)
        return None

    def value_animcatowned(self, value):
        return value

    def render_hhproblems(self, record):
        if record.house_hold_problems is not None:
            return ', '.join(record.house_hold_problems)
        return None
