from django import forms
from .models import Storage


class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = "__all__"