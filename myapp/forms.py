from django import forms
from .models import FoodCategory, Food
# from django.forms.widgets import DateInput

class FoodCategoryForm(forms.ModelForm):
    class Meta:
        model = FoodCategory
        fields = ['name']

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'category', 'amount', 'description']
