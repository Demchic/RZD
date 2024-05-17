from django import forms
from django.contrib.auth import get_user_model
from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesFrom(ModelForm):
    class Meta:
        user = get_user_model()
        model = Articles
        fields = ['department', 'sector', 'post', 'service', 'address', 'komm']
        widgets = {
            "department": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Департамент'
            }),
            "sector": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Полное наименование отдела/сектора'
            }),
            "post": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность'
            }),
            "service": forms.Select(attrs={
                'class': 'form-select mt-1',
                'style': 'height: 100%',
                'placeholder': 'Услуга'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес установки оборудования'
            }),
            "komm": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            })
        }
