from django import forms
from .models import Contact

"""
This class for make a form for contact view when you dont have the
model and you dont want to save the data in to the DB fo example you want to
sent that contact to the admin email
"""
# class ContactForm(forms.Form):
# name = forms.CharField()
# email = forms.EmailField()
# message = forms.CharField(widget=forms.Textarea)

"""
This class for make form for contact view when you want to send the 
email and save the contact to the DB
"""


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            "name",
            "email",
            "message",
        ]
