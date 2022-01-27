
from django import forms

class Fileuploadform(forms.Form):
    file_name = forms.FileField()

