from django import forms
from unlockk.models import Write

class WriteForm(forms.WriteForm):
    class Meta:
        model = Write
        fields = ['subject', 'content']