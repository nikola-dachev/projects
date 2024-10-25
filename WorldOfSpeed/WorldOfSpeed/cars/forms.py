from django import forms

from WorldOfSpeed.cars.models import Car


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_url'].widget.attrs['placeholder'] = "https://..."


class UpdateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']


class DeleteCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = "disabled"