from django import forms

class ConvoForm(forms.Form):
    convId = forms.CharField(max_length=25, required=True)