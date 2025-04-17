from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class StockTransferForm(forms.ModelForm):
    class Meta:
        model = StockTransfer
        fields = ['product', 'from_location', 'to_location', 'quantity']

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'location', 'password1', 'password2']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_super_admin = forms.BooleanField(required=False)
    is_location_admin = forms.BooleanField(required=False)
    location = forms.ChoiceField(choices=[('', '---------')] + list(LOCATION_CHOICES), required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'location', 'is_super_admin', 'is_location_admin']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_super_admin = self.cleaned_data['is_super_admin']
        user.is_location_admin = self.cleaned_data['is_location_admin']
        user.location = self.cleaned_data['location']

        # Apply privilege flags
        if user.is_super_admin:
            user.is_superuser = True
            user.is_staff = True
        elif user.is_location_admin:
            user.is_staff = True

        if commit:
            user.save()
        return user

