from django import forms

from WorldOfSpeed.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['username', 'email','age', 'password']


class UpdateProfileForm(forms.ModelForm):


    class Meta:
        model = Profile
        fields ='__all__'