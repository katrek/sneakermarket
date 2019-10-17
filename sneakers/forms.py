from django import forms
from .models import Sneakers


class SneakersForm(forms.ModelForm):
    class Meta:
        model = Sneakers
        fields = ['model_name', 'model_brand','model_price', 'model_photo']

