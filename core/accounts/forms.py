from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    '''
    This class for making the custom user create form
    '''
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput
    )

    '''
    That is the meta class for choosing the fields to show
    '''
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "is_staff",
            "is_active",
            "is_superuser",
            "is_verified",
            "groups",
            "user_permissions",
        )

    '''
    That function for check that two password same
    '''
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match.")

        return password2

    '''
    That function for encrypt the password
    '''
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user


class CustomUserChangeForm(forms.ModelForm):
    '''
    This class for making the custom user change form
    '''
    password = ReadOnlyPasswordHashField()

    '''
    That is the meta class for choosing the fields to show
    '''
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "password",
            "is_active",
            "is_staff",
            "is_superuser",
            "is_verified",
            "groups",
            "user_permissions",
            "last_login",
        )

    def clean_password(self):
        return self.initial["password"]