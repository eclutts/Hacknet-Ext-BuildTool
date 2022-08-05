from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class CompForm(forms.Form):
    node_id = forms.CharField(label='ID', max_length=255)
    name = forms.CharField(label="Name", max_length=255)