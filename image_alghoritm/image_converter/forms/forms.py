from django.forms import forms


class FileUploadForm(forms.Form):
    file_source = forms.FileField()