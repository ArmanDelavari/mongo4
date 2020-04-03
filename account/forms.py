from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User



class UserCreationForm(forms.ModelForm):    # hatman bayad namesh in bashe, forme sakhte karbar
        password1 = forms.CharField(label='password', widget=forms.PasswordInput)
        password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

        model = User
        fields = ('email', 'full_name')


        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
                raise forms.ValidationError('passwordha yeki nis')
            return cd['password2']

        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['password1'])  # hash mikone
            if commit:
                user.save()
            return user


class UserChangeForm(forms.ModelForm):   # forme taghire karbar
    password = ReadOnlyPasswordHashField()   # pass rp hash mikone
    class Meta:
        model = User
        fields = ('email', 'password', 'full_name')

    def clean_password(self):
        return self.initial['password']




# baraye login kardan
class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class UserRegistrationsForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))