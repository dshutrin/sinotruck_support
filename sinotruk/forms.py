from django import forms
from .models import *


class AddFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddFileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'document':
                self.fields[field].widget.attrs.update({'oninput': 'set_file_name'})
            if field != 'document':
                self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'required': 'required', 'placeholder': self.fields[field].label})

    class Meta:
        model = Document
        exclude = ('owner', )
