from django import forms
from .models import User
from django.contrib.auth import authenticate


class BasePasswordForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords don't match")
        return password2


class CreateUserForm(forms.ModelForm, BasePasswordForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username']

    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username']


class UpdatePasswordForm(forms.ModelForm, BasePasswordForm):
    class Meta:
        model = User
        fields = ['password', 'password1', 'password2']

    password = forms.CharField(widget=forms.PasswordInput, label='Current password')

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if not self.instance.check_password(password):
            raise forms.ValidationError('Incorrect password')
        return password

    def save(self, commit=True):
        password = self.cleaned_data.get('password1')
        user = super().save(commit=False)
        user.set_password(password)

        if commit:
            user.save()

        return user


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    password = forms.CharField(widget=forms.PasswordInput)
