from django import forms
from .models import *


class AddFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddFileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'document':
                self.fields[field].widget.attrs.update({'oninput': 'set_file_name()'})
            if field != 'document':
                self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'required': 'required', 'placeholder': self.fields[field].label})

    class Meta:
        model = Document
        exclude = ('owner', 'file_type', 'folder')


class EditUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'required': 'required', 'class': 'form-control-input'
            })

    class Meta:
        model = CustomUser
        exclude = (
            'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined', 'email'
        )


class EditManagerForm(EditUserForm):
    class Meta:
        model = CustomUser
        exclude = (
            'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined', 'email', 'dealer_name'
        )


class EditDealerForm(EditUserForm):
    class Meta:
        model = CustomUser
        exclude = (
            'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined', 'email', 'sub_role'
        )


class EditClientForm(EditUserForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'surname', 'email', 'clear_password', 'role')


class AddFolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        exclude = ('name', )


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = MessageDocument
        fields = ('document', )
