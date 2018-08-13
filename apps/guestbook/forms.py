from django import forms

from .models import Guestbook


class GuestbookForm(forms.ModelForm):
    class Meta:
        model = Guestbook
        fields = '__all__'
