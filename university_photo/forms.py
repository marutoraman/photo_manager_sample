from django import forms
from .models import Picture

class ProductForm(forms.ModelForm): #写真を送信するフォーム
    class Meta:
        model = Picture
        fields = ("description","picture",)
    