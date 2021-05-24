from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import Hospital, Donor
from django.views.generic.edit import UpdateView


class RegisterFormHosp(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2', 'groups']

class RegisterFormDonor(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2', 'groups']

class HospProf(ModelForm):
    class Meta:
        model = Hospital
        fields = ['hospid','name', 'email','contact','location','Apositive',
        'Anegative','Bpositive','Bnegative','ABpositive','ABnegative',
        'Opositive','Onegative']

class DonorProf(ModelForm):
    class Meta:
        model = Donor
        fields = ['donorid','name', 'email','contact','location','bloodgroup','status']

class HospContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    recipient_list = forms.EmailField(required=True)
    subject = forms.CharField(required=True, help_text="Enter blood group and pints required")
    message = forms.CharField(widget=forms.Textarea, required=True, help_text="A brief description")


class DonorContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    recipient_list = forms.EmailField(required=True)
    subject = forms.CharField(required=True, help_text="Enter blood group required")
    message = forms.CharField(widget=forms.Textarea, required=True, help_text="A brief description")


class ScheduleDonationForm(forms.Form):
    from_email = forms.EmailField(required=True)
    recipient_list = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    message = forms.CharField(widget=forms.Textarea, required=True, help_text="Message")

    