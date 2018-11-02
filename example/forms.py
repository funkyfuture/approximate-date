from django import forms
from django_date_extensions.forms import PrettyDateField, ApproximateDateFormField


class DatesForm(forms.Form):
    near_future = PrettyDateField(future=True)
    near_past = PrettyDateField(future=False)
    just_a_date = PrettyDateField()
    approximate = ApproximateDateFormField()

    def clean(self):
        self.safe_cleaned_data = self.cleaned_data
        return self.cleaned_data
