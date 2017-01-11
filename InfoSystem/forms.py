from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Parent

class NameForm(forms.Form):
    name = forms.CharField(label="Your Roll Num", max_length=128)

class ParentRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    name = forms.CharField(required=True)
    email = forms.EmailField(required=False)
    mobile = forms.CharField(required=True)

    def save(self, commit=True):
        user = super(ParentRegistrationForm, self).save(commit=False)
        user.name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        try:
            par = Parent.objects.get(mobile=self.cleaned_data['mobile'])
            par.email = user.email
            par.user = user
            return user
        except:
            pass