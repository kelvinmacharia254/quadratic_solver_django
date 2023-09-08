from django import forms


class QuadraticForm(forms.Form):
    field_a = forms.FloatField(label = "coefficient a :")
    field_b = forms.FloatField(label = "coefficient b :")
    field_c = forms.FloatField(label = "coefficient c :")

    def clean_field_a(self):
        field_a_value = self.cleaned_data['field_a']

        # Check if the value is zero
        if field_a_value == 0:
            raise forms.ValidationError("Coefficient a cannot be zero")

        return field_a_value