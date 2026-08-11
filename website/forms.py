# sendemail/forms.py
from django import forms


class ContactForm(forms.Form):
    site_num = forms.IntegerField()
    site_loc = forms.CharField(max_length=100,required=False)
    date = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone = forms.CharField(max_length=100)
    issue = forms.MultipleChoiceField(
        choices=[
            ("tower","Tower"),
            ("ground_maintenance","Ground Maintenance"),
            ("locks_access","Locks/Access"),
            ("access_drive","Access Drive"),
            ("other","Other"),
        ],
        widget=forms.CheckboxSelectMultiple,
    )
    other_issue = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea,required=False)