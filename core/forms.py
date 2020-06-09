from django import forms


class NumeroForm(forms.Form):
    tipo = forms.ChoiceField(choices=(("BINARIO", 'Binário'), ("DECIMAL", 'Decimal')), label='Tipo')
    numero = forms.IntegerField(label='Número')
