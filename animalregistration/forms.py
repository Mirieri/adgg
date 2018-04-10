from django import forms


class OptionsForm(forms.Form):
    OPTIONS = (
        ('e', 'EXACT'),
        ('a', 'AND'),
        ('o', 'OR')
    )

    options = forms.ChoiceField(
        choices=OPTIONS,
        initial='o',
        widget=forms.RadioSelect(),
        required=False
    )
