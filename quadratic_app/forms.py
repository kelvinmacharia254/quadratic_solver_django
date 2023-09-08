from django import forms


class QuadraticForm(forms.Form):
    field_a = forms.FloatField(label = "coefficient a :")
    field_b = forms.FloatField(label = "coefficient b :")
    field_c = forms.FloatField(label = "coefficient c :")