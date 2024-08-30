from django.forms import ModelForm
from .models import *
from django import forms


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['firstname','lastname']